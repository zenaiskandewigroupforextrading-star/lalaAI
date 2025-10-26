🌍 Overview
EduMate — also known as LalaAI — is a next-generation AI learning companion built to continuously evolve, learn, and adapt over time.
It merges the intelligence of a local offline knowledge base with the flexibility of online AI processing, creating a hybrid system that bridges offline and online intelligence.
Unlike traditional chatbots, EduMate is designed with a Self-Modifying System (SMS) — a mechanism that allows the AI to refine its own logic and expand its knowledge base automatically without constant user input.
EduMate is developed using Flask, Python, NLTK, and the Google Gemini API, while maintaining full compatibility for offline use via a local JSON knowledge base.
🎯 Vision & Mission
Vision:
To create an AI system capable of autonomous learning and adaptation — a digital being that grows smarter, more capable, and more helpful every day.
Mission:
To make AI accessible and meaningful for education, self-learning, and intelligent assistance — all while giving users full control over its data, logic, and evolution.
💡 Core Features
1. Hybrid Intelligence System
Combines offline database (kamus_offline.json) and online AI (Gemini API).
When offline, EduMate relies entirely on its stored dictionary and NLP system.
When online, it connects to Google Gemini for advanced reasoning.
2. Self-Modifying System (SMS)
Automatically improves its reasoning logic and text-processing behavior.
Learns from past interactions and optimizes itself for better future responses.
Limited access to self-modification (cannot alter core security or logic core).
3. Offline-First Architecture
Runs seamlessly in environments like Termux, Proot Ubuntu, or local servers.
Works perfectly without internet, making it ideal for education in low-connectivity regions.
4. Smart Learning Companion
Specialized for education, learning, and research assistance.
Supports explanation generation, concept simplification, and tutoring-like interactions.
5. Expandable & Open
Users and developers can add custom knowledge directly into the JSON dictionary.
Supports integration with additional APIs, local datasets, and NLP modules.
## Hybrid AI System – LalaAI Web

LalaAI is an intelligent web chatbot developed by M.idris.pratama.
It combines three AI layers:

1. **Offline Dictionary (JSON)** – Fast and local response base.
2. **Gemini API Integration** – Cloud-based large language understanding.
3. **Chrome Built-in AI (Proofreader API)** – Local client-side AI running directly in Chrome using the new AI APIs.

This hybrid approach allows LalaAI to operate both online and offline, 
providing privacy, flexibility, and adaptive intelligence.

🧩 Tech Stack
Component
Technology
Backend
Python (Flask)
NLP
NLTK (punkt tokenizer)
Online AI
Google Gemini API
Offline Knowledge
JSON Database (kamus_offline.json)
Frontend
HTML, CSS, JS (Flask Jinja2 Templates)
Hosting
Ngrok / Localhost / Any Flask-compatible host
Developer Environment
Termux + Ubuntu (Proot)
⚙️ How EduMate Works
User inputs a question via the chat interface.
EduMate first searches the offline dictionary (kamus_offline.json).
If the question is not found, it queries the Gemini API.
Gemini returns a structured response → EduMate formats it beautifully in chat view.
The AI can optionally store new Q&A pairs into the JSON file for future offline recall.
Over time, EduMate’s Self-Modifying System refines its text understanding and language patterns.
🧠 Example Interaction
User:
Apa itu Machine Learning?
EduMate (Bot):
Machine Learning adalah cabang dari kecerdasan buatan yang memungkinkan sistem belajar dari data tanpa pemrograman eksplisit. Sistem ini mengidentifikasi pola dan meningkatkan performa berdasarkan pengalaman.
🚀 Installation & Setup
1. Clone or Copy the Project
Salin kode
Bash
git clone https://github.com/midrispratama/EduMate.git
cd EduMate
2. Install Dependencies
Salin kode
Bash
pip install -r requirements.txt
3. Run the Application
Salin kode
Bash
python app.py
4. Access the AI
Open your browser and go to:
Salin kode

http://127.0.0.1:5000
🧩 File Structure
Salin kode

EduMate/
│
├── app.py
├── gemini_api.py
├── kamus_offline.json
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── chatroom.html
│   ├── tentang.html
│
├── static/
│   ├── css/
│   ├── js/
│
├── requirements.txt
└── README.md
🧪 Testing Instructions
Launch the Flask app using:
Salin kode
Bash
python app.py
Open the chatbot in a browser.
Ask questions in Indonesian or English.
Test both offline mode and online mode by toggling the Gemini API key in gemini_api.py.
(Optional) Check kamus_offline.json to verify that new data is stored automatically.
🛠️ Future Development
Add multi-language translation via Google Translate API
Build integrated Text-to-Speech and Speech-to-Text
Create a full autonomous learning model that trains from Wikipedia articles
Develop a mobile-friendly UI with animated responses
Integrate “Memory Vault” for storing long-term user-AI history
🧾 License
This project is licensed under the MIT License.
Copyright © 2025
M. Idris Pratama
❤️ Acknowledgments
Special thanks to:
Google Gemini API Team
Flask & NLTK Open Source Community
All independent AI developers inspiring the new era of intelligent agents
