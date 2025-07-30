import warnings

from dotenv import load_dotenv

import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

warnings.filterwarnings(action='ignore')
llm1 = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

prompt = PromptTemplate(
  input_variables=["country"],
  template= "{country}의 수도는 어디야?",
)

chain = LLMChain(llm=llm1, prompt=prompt) #프롬프트와 모델을 체인으로 연결
print(chain.run("대한민국"))