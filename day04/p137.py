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

from langchain import ConversationChain
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="진희는 강아지를 한마리 키우고 있습니다.")
conversation.predict(input="영수는 고양이를 두마리 키우고 있습니다.")
conversation.predict(input="진희와 영수가 키우는 동물은 총 몇마리?")
conversation.predict(input="참 잘했어요")