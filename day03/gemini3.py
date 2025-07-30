import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL.Image



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


long_text = """

대규모 언어 모델(Large Language Model, LLM)은 방대한 양의 텍스트 데이터를 학습하여 인간의 언어를 이해하고 생성하는 인공지능 모델입니다. 이들은 주로 딥러닝 기술, 특히 트랜스포머 아키텍처를 기반으로 합니다. LLM은 문장 완성, 번역, 요약, 질의응답 등 다양한 자연어 처리(NLP) 작업에서 뛰어난 성능을 보이며, 최근에는 코드 생성이나 이미지 설명과 같은 멀티모달 능력까지 확장되고 있습니다. 

"""

prompt = f"다음 텍스트를 3문장으로 요약해 줘:\n\n{long_text}"

response = model.generate_content(prompt)

print("--- 텍스트 요약 ---")

print(response.text)
