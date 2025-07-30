import warnings

from dotenv import load_dotenv

import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

warnings.filterwarnings(action='ignore')
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

#프롬프트1 정의
prompt1 = PromptTemplate(
    input_variables=['sentence'],
    template="다음 문장을 한글로 번역하세요.\n\n{sentence}"
)
#번역(체인1)에 대한 모델
chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="translation")

#프롬프트2 정의
prompt2 = PromptTemplate.from_template(
    "다음 문장을 한 문장으로 요약하세요.\n\n{translation}"
)
#요약(체인2)에 대한 모델
chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="summary")

from langchain.chains import SequentialChain
all_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=['sentence'],
    output_variables=['translation','summary'],
)
sentence="""
One limitation of LLMs is their lack of contextual information (e.g., access to some specific documents or emails). You can combat this by giving LLMs access to the specific external data.
For this, you first need to load the external data with a document loader. LangChain provides a variety of loaders for different types of documents ranging from PDFs and emails to websites and YouTube videos.
"""
print(all_chain(sentence))