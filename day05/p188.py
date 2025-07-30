import pandas as pd #파이썬 언어로 작성된 데이터를 분석 및 조작하기 위한 라이브러리

#csv 파일을 데이터프레임으로 가져오기
df = pd.read_csv('data/booksv_02.csv') #booksv_02.csv 파일이 위치한 경로 지정
print(df.head())


from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#에이전트 생성
agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model='gpt-4o'),  #gpt-3.5-turbo 사용
    df,             #데이터가 담긴 곳
    verbose=False,  #추론 과정을 출력하지 않음
    agent_type=AgentType.OPENAI_FUNCTIONS,
    allow_dangerous_code=True,
)
agent.run('어떤 제품의 ratings_count가 제일 높아?')

agent.run('가장 최근에 출간된 책은?')