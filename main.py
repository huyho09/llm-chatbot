import streamlit as st
import pandas as pd
import json
from models.chatbot_memory import get_chat_history, store_message
from services.openai_llm import get_chatbot_response
from services.external_search import search_product_online

st.set_page_config(page_title="AI Sales Chatbot", layout="wide")

st.title("🤖 AI Sales Chatbot")

# Sidebar - Product Categories
st.sidebar.title("Product Categories")
categories = [
    "Assembly Technology", "Electric Drives and Controls", "Gear Technology",
    "Industrial Hydraulics", "Linear Motion Technology", "Mobile Hydraulics and Electronics",
    "Moulding and Casting Technologies", "Tightening Technology", "Resistance Welding",
    "Mobile Robotics", "Hägglunds", "Kassow Robots"
]
selected_category = st.sidebar.selectbox("Select a Category", categories)

# Sidebar - Customer Inquiry
st.sidebar.subheader("Customer Inquiry")
customer_name = st.sidebar.text_input("Customer Name")
customer_email = st.sidebar.text_input("Customer Email")

# Load and filter product database
df = pd.read_csv("data/sample_products.csv")
filtered_products = df[df["category"] == selected_category]
st.subheader(f"🛒 Available {selected_category} Products")
st.dataframe(filtered_products)

# Chatbot Section
st.subheader("💬 Chat with the AI Sales Agent")

# Retrieve chat history and ensure it's a list of dictionaries
chat_history = get_chat_history()

# ✅ Fix: Handle empty chat history
if not chat_history:
    chat_history = []  # Initialize empty list if history is empty
elif isinstance(chat_history, str):
    try:
        chat_history = json.loads(chat_history)  # Convert from JSON if necessary
    except json.JSONDecodeError:
        chat_history = []  # If JSON fails to decode, reset to empty list

for chat in chat_history:
    if isinstance(chat, dict) and "input" in chat and "output" in chat:
        st.text_area(f"{chat['input']}", value=chat['output'], height=100)

# User Input
user_input = st.text_input("Ask about a product:", "")

if user_input:
    response = get_chatbot_response(user_input)
    store_message(user_input, response)
    st.text_area("Chatbot:", value=response, height=100)

    # External Search
    st.subheader("🔍 Related Web Search Results")
    results = search_product_online(user_input)
    for res in results:
        st.write(f"- [{res}]({res})")

# Lead Capture
if st.sidebar.button("Submit Inquiry"):
    with open("data/leads.txt", "a") as file:
        file.write(f"{customer_name}, {customer_email}, {selected_category}\n")
    st.sidebar.success("Inquiry Submitted!")
