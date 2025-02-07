from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history")

def store_message(user, bot):
    memory.save_context({"input": user}, {"output": bot})

def get_chat_history():
    return memory.load_memory_variables({})["chat_history"]
