import openai
from openai import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

messages = [
    {"role": "system", "content": "너는 친절한 한국어 선생님이야"}
]
while True:

    user_input = input("👤 사용자: ")

    if user_input.lower() in ["exit", "quit"]:

        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(

        model='gpt-4o',

        messages=messages

    )

    reply = response.choices[0].message.content

    print("🤖 챗봇:", reply)

    messages.append({"role": "assistant", "content": reply})
