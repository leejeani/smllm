import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL.Image



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

korean_text = "안녕하세요, Gemini를 사용하여 파이썬 프로그램을 개발하는 방법에 대해 배우고 있습니다."

prompt = f"다음 한국어 문장을 영어로 번역해 줘:\n\n{korean_text}"

response = model.generate_content(prompt)

print("\n--- 번역 ---")
print(response.text)
