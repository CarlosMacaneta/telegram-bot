import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get('GEMINI_TOKEN_KEY'))

model = genai.GenerativeModel(os.environ.get('GEMINI_MODEL_NAME'))

response = model.generate_content("Write a story about an AI and magic")
print(response.text)