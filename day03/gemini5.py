import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL.Image



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

question = "인공지능이란 무엇인가요?"

prompt = f"'{question}'에 대해 설명해 줘."

response = model.generate_content(prompt)

print("\n--- 질문-응답 ---")

print(response.text)