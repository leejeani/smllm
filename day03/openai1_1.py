from llm.MyApi import openAiModel, openAiModelArg, makeMsg

def openAiTest(str):
    msg = makeMsg("너는 친절한 한국어 선생님이야",str)
    response = openAiModelArg("gpt-4o",msg)
    print(response)

if __name__ == "__main__":
    openAiTest("한국의 수도는 어디야")