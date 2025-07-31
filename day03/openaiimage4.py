import urllib

from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.edit(
    model="dall-e-2",
    image=open("sample.png", "rb"),
    mask=open("sample-mask.png", "rb"),
    prompt="add a Christmas tree, Sigma 24mm f/8",
    n=1,
    size="1024x1024",
)

image_url = response.data[0].url
urllib.request.urlretrieve(image_url, "edited_output.png")

