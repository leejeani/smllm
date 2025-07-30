from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


# 모델 로드
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_output_tokens=200,
    google_api_key=GOOGLE_API_KEY
)

messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "LLM은 어떤 원리로 작동하나요? 100자 이내로 설명해주세요."},
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)