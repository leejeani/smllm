from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.generate(

    model="dall-e-3",

    prompt="a white siamese cat and black dog",

    size="1024x1024",

    quality="standard",

    n=1,

)

image_url = response.data[0].url

print(image_url)
print(response)

import requests

save_path = "dog.png"

response = requests.get(image_url, stream=True)

if response.status_code == 200:

    with open(save_path, 'wb') as file:

        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

    print(f"이미지 다운로드 완료: {save_path}")

else:

    print(f"이미지 다운로드 실패. HTTP 상태 코드: {response.status_code}")