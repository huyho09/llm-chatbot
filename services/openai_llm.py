import openai
import os
#from config import OPENAI_API_KEY
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#openai.api_key = OPENAI_API_KEY

def get_chatbot_response(user_input):
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content
