import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL.Image



load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

img = PIL.Image.open("dog.png")
response = model.generate_content(
    [
        "제시된 이미지를 3문장 이내의 한국어로 설명해주세요.",
        img,
    ]
)

print(response.text)