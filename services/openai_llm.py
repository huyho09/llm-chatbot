import openai
import os
#from config import OPENAI_API_KEY
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("k-proj-IZqieVr1h1HMxu5f3TOHTZKUqwBEnqJNWB6Qevi3S6IgXaz67vaMGXrGaG20sD1VGbYrHjp4urT3BlbkFJGoPnzv0e5k_TTI0FSU1gLAl-gZE0qzi3fqlsZM7aviSagVnj8Nz2aaXU5l6fM01afiwes-qXAA")

#openai.api_key = OPENAI_API_KEY

def get_chatbot_response(user_input):
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content
