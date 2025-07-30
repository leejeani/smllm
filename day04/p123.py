import warnings
from llm.MyLLM import getChatOpenAI, getGenAI
from langchain.model_laboratory import ModelLaboratory

warnings.filterwarnings(action='ignore')

llm1 = getChatOpenAI()
llm = getGenAI()

modal_lab = ModelLaboratory.from_llms([llm1,llm])
modal_lab.compare("대한민국의 가을은 몇 월부터 몇 월까지야?")
