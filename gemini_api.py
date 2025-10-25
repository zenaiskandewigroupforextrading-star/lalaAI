import google.generativeai as genai

genai.configure(api_key="AIzaSyBpRuqZBSrYChPhIqFbkVZ7Z8ubDN2HMc0")

model = genai.GenerativeModel("models/gemini-1.5-flash")

def tanya_ke_gemini(pertanyaan):
    try:
        response = model.generate_content(pertanyaan)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"
