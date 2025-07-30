import google.generativeai as genai


from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


from PIL import Image
import requests
from io import BytesIO


# 이미지 URL에서 이미지 로드 (예시: 실제 이미지 URL 사용 필요)

image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-9qyO8DBfZVE7lQkjKIV1E3u9/user-6iEJ0m5gbHH0s0nAsMuCmNs6/img-QASE3O3BPZGtzBbWetlCmOXq.png?st=2025-07-29T06%3A07%3A18Z&se=2025-07-29T08%3A07%3A18Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-29T05%3A58%3A18Z&ske=2025-07-30T05%3A58%3A18Z&sks=b&skv=2024-08-04&sig=CkI1F6/7uS0aVBLRdFB%2BstcZ4fSHRf1zuxFGBSWIi6I%3D" # 실제 이미지 URL로 교체

response_image = requests.get(image_url)

img = Image.open(BytesIO(response_image.content))

response = model.generate_content(
    [
        "제시된 이미지를 3문장 이내의 한국어로 설명해주세요.",
        img,
    ]
)

print(response.text)
