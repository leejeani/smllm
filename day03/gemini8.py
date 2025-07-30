import google.generativeai as genai


from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


from PIL import Image


# 이미지 URL에서 이미지 로드 (예시: 실제 이미지 URL 사용 필요)

image = Image.open('./pocari.jpg')

response = model.generate_content(
    [
        "음료의 영양성분표야.제품명,  칼로리, 영양성분 아래 내용들 좀 정리해줘.",
        image,
    ]
)

print(response.text)
