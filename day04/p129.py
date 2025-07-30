import warnings

from langchain_community.document_loaders import PyPDFLoader
warnings.filterwarnings(action='ignore')
loader = PyPDFLoader("./The_Adventures_of_Tom_Sawyer.pdf")
document = loader.load()

print(document[5].page_content[:5000])
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
embeddings = OpenAIEmbeddings() #임베딩 처리
db = FAISS.from_documents(document, embeddings)

from langchain_community.chat_models import ChatOpenAI
llm1 = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

from langchain.chains import RetrievalQA
retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=llm1,
    chain_type="stuff",
    retriever=retriever)

query = "마을 무덤에 있던 남자를 죽인 사람은 누구니?"
result = qa({"query": query})
print(result['result'])