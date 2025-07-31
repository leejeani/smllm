import urllib

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

image_url = response.data[0].url
print(image_url)


urllib.request.urlretrieve(image_url, "generated_image.jpg")

