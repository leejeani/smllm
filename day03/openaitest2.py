from openai import OpenAI
from IPython.display import Image, display, Audio, Markdown
import base64

from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

IMAGE_PATH = "./amd.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


if __name__ == "__main__":
    base64_image = encode_image(IMAGE_PATH)

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
            {"role": "user", "content": [
                {"type": "text", "text": "보드 위에 적혀있는 M과 G+C 라는 문자의 의미를 알려주세요."},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpg;base64,{base64_image}"}
                }
            ]}
        ],
        temperature=0.0,
    )

    print(response.choices[0].message.content)

