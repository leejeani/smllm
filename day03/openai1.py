from llm.MyApi import openAiModel

def openAiTest(str):
    client = openAiModel()
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "너는 친절한 한국어 선생님이야"},
            {"role": "user", "content": str},
        ]
    )
    print(response)
    print(response.choices[0].message.content)

if __name__ == "__main__":
    openAiTest("한국의 수도는 어디야")