
import warnings
from llm.MyLLM import getChatOpenAI
warnings.filterwarnings(action='ignore')

if __name__ == '__main__':
    llm1 = getChatOpenAI()

    prompt = "진희는 강아지를 키우고 있습니다. 진희가 키우는 동물은?"

    print(llm1.invoke(prompt).content)