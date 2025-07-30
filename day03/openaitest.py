


import openai
from openai import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


openai.api_key = OPENAI_API_KEY

def myfnc(api_key):
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "질문에 대한 답변은 항상 한 문장으로 작성해주세요.",
            },
            {
                "role": "user",
                "content": "위키북스에 대해서 말해줘.",
            },
        ],
        max_tokens=100,
    )
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    myfnc(OPENAI_API_KEY)