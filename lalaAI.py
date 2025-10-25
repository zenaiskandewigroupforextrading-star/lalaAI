# lalaAI.py (versi modular)
import json
import random
import re
import wikipedia
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set bahasa Wikipedia
wikipedia.set_lang("id")

# Load kamus
try:
    with open("kamus_offline.json", "r") as file:
        kamus = json.load(file)
except FileNotFoundError:
    kamus = {}

# Load rating (opsional)
try:
    with open("rating.json", "r") as file:
        rating_data = json.load(file)
except FileNotFoundError:
    rating_data = {}

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
        bersih = re.sub(r"siapa itu|apa itu|siapa|apa", "", query.lower()).strip().title()
        return wikipedia.summary(bersih, sentences=2, auto_suggest=True)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Ada beberapa kemungkinan: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return f"Maaf, tidak ada halaman yang cocok dengan '{query}'."
    except Exception as e:
        return f"Error Wikipedia: {e}"

def jawab_pertanyaan(user_input):
    match = find_best_match(user_input.lower(), kamus)
    if match:
        return pilih_jawaban(kamus[match])
    else:
        return search_wikipedia(user_input)
