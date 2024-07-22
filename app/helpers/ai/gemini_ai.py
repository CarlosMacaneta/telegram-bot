import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GEMINI_TOKEN_KEY'))

model = genai.GenerativeModel(os.environ.get('GEMINI_MODEL_NAME'))

def get_gemini_model():
    return model