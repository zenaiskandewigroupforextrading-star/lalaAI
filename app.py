from flask import Flask, render_template, request, redirect, url_for, session
import json, wikipedia
import random
import numpy as np
import os
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gemini_api import tanya_ke_gemini

app = Flask(__name__)
app.secret_key = 'rahasia123'

wikipedia.set_lang("id")

kamus_path = 'kamus_offline.json'
users_path = 'users.json'

# Load kamus
if os.path.exists(kamus_path):
    with open(kamus_path) as f:
        kamus = json.load(f)
else:
    kamus = {}

# Load users
if os.path.exists(users_path):
    with open(users_path) as f:
        users = json.load(f)
else:
    users = {}

# Fungsi AI

def find_best_match(query, dictionary):
    if not dictionary:
        return None
    texts = list(dictionary.keys())
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts + [query])
    similarities = cosine_similarity(vectors[-1], vectors[:-1])
    best_match_idx = np.argmax(similarities)
    if similarities[0, best_match_idx] > 0.4:
        return texts[best_match_idx]
    return None
    
def pilih_jawaban(jawaban):
    if isinstance(jawaban, list):
        return random.choice(jawaban)
    return jawaban

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return 'Maaf, aku tidak menemukan jawaban di kamus maupun Wikipedia.'

def jawab_pertanyaan(input_user):
    input_user = input_user.lower()
    
    # 1. Cek Kamus
    match = find_best_match(input_user, kamus)
    if match:
        return pilih_jawaban(kamus[match])

    # 2. Coba ke Gemini API
    jawaban_gemini = tanya_ke_gemini(input_user)
    if jawaban_gemini and not "Gagal" in jawaban_gemini:
        return jawaban_gemini


    # Kalau tidak ketemu, cari di transkrip YouTube
    best_transcript_match = None
    best_score = 0.0

    if os.path.exists('transkrip_youtube'):
        for filename in os.listdir('transkrip_youtube'):
            if filename.endswith('.txt'):
                with open(os.path.join('transkrip_youtube', filename), 'r', encoding='utf-8') as f:
                    content = f.read().lower()

                    # Pisahkan isi menjadi kalimat
                    sentences = content.split('.')

                    # Pakai TF-IDF untuk cari kalimat paling mirip
                    vectorizer = TfidfVectorizer()
                    vectors = vectorizer.fit_transform(sentences + [input_user])
                    similarities = cosine_similarity(vectors[-1], vectors[:-1])

                    # Cari kalimat dengan similarity tertinggi
                    max_idx = similarities.argmax()
                    max_score = similarities[0, max_idx]

                    if max_score > best_score and max_score > 0.3:  # ambang batas kemiripan
                        best_score = max_score
                        best_transcript_match = sentences[max_idx]

    if best_transcript_match:
        return f"Jawaban dari transkrip: {best_transcript_match.strip()}"

    # Kalau tetap tidak ketemu, fallback ke Wikipedia
    return search_wikipedia(input_user)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            session['email'] = email
            session['chat_history'] = []
            return redirect(url_for('home'))
        else:
            error = 'Email atau password salah!'
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        if email and password:
            users[email] = password
            with open(users_path, 'w') as f:
                json.dump(users, f, indent=2)
            message = 'Registrasi berhasil! Silakan login.'
    return render_template('register.html', message=message)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'email' not in session:
        return redirect(url_for('login')) 
    
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        question = request.form['question'].strip()
        if question:
            answer = jawab_pertanyaan(question)
            session['chat_history'].append({'user': question, 'bot': answer})
            session.modified = True

    return render_template('home.html', email=session['email'], chat=session['chat_history'])

@app.route('/training', methods=['GET', 'POST'])
def training():
    if 'email' not in session:
        return redirect(url_for('login'))

    message = ''
    if request.method == 'POST':
        question = request.form['question'].strip().lower()
        answer = request.form['answer'].strip()
        if question and answer:
            if question in kamus:
                if not isinstance(kamus[question], list):
                    kamus[question] = [kamus[question]]
                kamus[question].append(answer)
            else:
                kamus[question] = answer
            with open(kamus_path, 'w') as f:
                json.dump(kamus, f, indent=2)
            message = 'Berhasil disimpan ke kamus!'

    return render_template('training.html', message=message)

@app.route('/tambah_database', methods=['GET', 'POST'])
def tambah_database():
    if 'email' not in session:
        return redirect(url_for('login'))

    message = ''
    if request.method == 'POST':
        if 'file' not in request.files:
            message = 'Tidak ada file dipilih!'
        else:
            file = request.files['file']
            if file.filename == '':
                message = 'File kosong!'
            elif file and file.filename.endswith('.txt'):
                filename = secure_filename(file.filename)
                save_path = os.path.join('transkrip_youtube', filename)
                file.save(save_path)
                message = 'Transkrip berhasil di-upload!'
            else:
                message = 'Format file harus .txt!'
    return render_template('tambah_database.html', message=message)

@app.route('/tentang')
def tentang():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('tentang.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)    
                               
