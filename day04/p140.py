import warnings

from dotenv import load_dotenv

import os
warnings.filterwarnings(action='ignore')
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate


llm = ChatOpenAI(temperature=0, model_name='gpt-4o')

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

tools = load_tools(["wikipedia", "llm-math"], llm=llm) #llm-math의 경우 나이 계산을 위해 사용
agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         description='계산이 필요할 때 사용',
                         verbose=True)

print(agent.run("트럼프가 태어난 해는? 2025년도 트럼프는 몇 살? 한국어로 답해줘"))