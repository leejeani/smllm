
import warnings
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_community.chat_models import ChatOpenAI
if __name__ == '__main__':
    warnings.filterwarnings(action='ignore')
    llm1 = ChatOpenAI(temperature=0, model_name='gpt-4o')


    output_parser = CommaSeparatedListOutputParser()  # 파서 초기화
    format_instructions = output_parser.get_format_instructions()  # 출력 형식 지정

    prompt = PromptTemplate(
        template="7개의 팀을 보여줘 {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )

    query = "한국의 야구팀은?"

    # 출력 결과 생성
    output = llm1.predict(text=prompt.format(subject=query))

    # 출력에 대한 포맷 변경
    parsed_result = output_parser.parse(output)
    print(parsed_result)