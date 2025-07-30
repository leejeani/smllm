from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# 주어진 이미지를 3개로 변형해본다.

response = client.images.create_variation(

    model="dall-e-2",

    image=open("dog.png", "rb"),

    n=3,

    size="1024x1024"

)

import requests

# 이미지 저장

for n, data in enumerate(response.data):

    print(data.url)

    save_path = f"dog_variation_{n}.png"

    response = requests.get(data.url, stream=True)

    if response.status_code == 200:

        with open(save_path, 'wb') as file:

            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)

        print(f"이미지 다운로드 완료: {save_path}")

    else:

        print(f"이미지 다운로드 실패. HTTP 상태 코드: {response.status_code}")