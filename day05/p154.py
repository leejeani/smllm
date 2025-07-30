from llm.MyLLM import getOpenAIEmbeddings, getChatOpenAI
from langchain.document_loaders import TextLoader
documents = TextLoader("data/AI.txt").load()

from langchain.text_splitter import RecursiveCharacterTextSplitter

# 문서를 청크로 분할
def split_docs(documents,chunk_size=1000,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

# docs 변수에 분할 문서를 저장
docs = split_docs(documents)
print(docs)

#OpenAI의 임베딩 모델 사용
embeddings = getOpenAIEmbeddings()

# Chromdb에 벡터 저장, 저장 장소는 d:/data
from langchain.vectorstores import Chroma
db = Chroma.from_documents(docs, embeddings, persist_directory="data")

llm = getChatOpenAI()

# Q&A 체인을 사용하여 쿼리에 대한 답변 얻기
from langchain.chains.question_answering import load_qa_chain
chain = load_qa_chain(llm, chain_type="stuff",verbose=True)

# 쿼리를 작성하고 유사성 검색을 수행하여 답변을 생성,따라서 txt에 있는 내용을 질의해야 합니다
query = "AI란?"
matching_docs = db.similarity_search(query)
answer =  chain.run(input_documents=matching_docs, question=query)
print(answer)
