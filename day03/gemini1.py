import google.generativeai as genai


from dotenv import load_dotenv
import os
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


response = model.generate_content("한국의 수도는 어디야 ")

print(response.text)