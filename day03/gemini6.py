import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL.Image



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

code_prompt = "Python으로 피보나치 수열을 계산하는 함수를 작성해 줘."

response = model.generate_content(code_prompt)

print("\n--- 코드 생성 ---")

print(response.text)

code_explanation_prompt = "다음 Python 코드의 기능을 설명해 줘:\n\n```python\ndef factorial(n):\n if n == 0:\n return 1\n else:\n return n * factorial(n-1)\n```"

response = model.generate_content(code_explanation_prompt)

print("\n--- 코드 설명 ---")

print(response.text)