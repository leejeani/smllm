import google.generativeai as genai


from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat(history=[])

print("\n--- Gemini 챗봇 시작 ---")

while True:

        user_message = input("나: ")

        if user_message.lower() == '종료':

                break

        response = chat.send_message(user_message)

        print("Gemini:", response.text)

print("--- 챗봇 종료 ---")
print(chat.history)
