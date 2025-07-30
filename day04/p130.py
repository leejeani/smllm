import warnings

from dotenv import load_dotenv

import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings() #임베딩 처리
text = "진희는 강아지를 키우고 있습니다. 진희가 키우고 있는 동물은?"
text_embedding = embeddings.embed_query(text)
print(text_embedding)