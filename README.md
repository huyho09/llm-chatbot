# AI Sales Chatbot for Industrial Products

## 📌 Project Overview
This project is an **AI-powered chatbot** designed to **replace sales agents** for selling industrial products. The chatbot assists users by:
- Providing product information.
- Answering customer inquiries.
- Fetching relevant data using **DuckDuckGo search**.
- Capturing lead information for future sales.
- Displaying available products by category.

The application is built with **Python**, **Streamlit**, **OpenAI API**, and **SQLAlchemy**, ensuring a robust and scalable solution for industrial sales automation.

---

## 🏗️ Project Architecture
```
                         +------------------------+
                         |    User Interface      |   (Streamlit)
                         +-----------+------------+
                                     |
                                     v
                         +------------------------+
                         |    LLM Chatbot Core    |   (LangChain, OpenAI API)
                         +-----------+------------+
                                     |
              ------------------------------------------------
             |                        |                      |
+---------------------+  +--------------------+  +-----------------------+
| Knowledge Retrieval |  | Product Database   |  | External Search API   |
| (LangChain Memory)  |  | (SQLAlchemy + SQL) |  | (DuckDuckGo Search)   |
+---------------------+  +--------------------+  +-----------------------+
```

---

## 📂 Folder Structure
```
ai_sales_agent/
│── app.py                     # Main Streamlit application
│── config.py                   # API keys & configuration
│── requirements.txt             # Python dependencies
│── .env                         # Environment variables
│
├───data/
│   ├── sample_products.csv      # 1,500+ sample product data
│   ├── database.sqlite          # SQLite database
│
├───models/
│   ├── product_model.py         # SQLAlchemy models
│   ├── chatbot_memory.py        # Chatbot memory storage
│
├───services/
│   ├── openai_llm.py            # OpenAI GPT integration
│   ├── knowledge_base.py        # Knowledge retrieval from database
│   ├── external_search.py       # DuckDuckGo integration
│   ├── db_service.py            # SQL database queries
│
├───utils/
│   ├── data_loader.py           # Data loading utilities
│   ├── logging_config.py        # Logging setup
│
└───static/
    ├── logo.png                 # Branding logo
    ├── styles.css               # Custom CSS styles
```

---

## 🛠️ Installation & Setup

### **1️⃣ Prerequisites**
- Python 3.10+
- OpenAI API Key
- Virtual Environment (optional but recommended)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/huyho09/llm-chatbot
cd llm-chatbot
```

### **3️⃣ Create a Virtual Environment**
```sh
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate     # For Windows
```

### **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **5️⃣ Set Up API Keys**
Create a **.env** file and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### **6️⃣ Initialize the Database**
```sh
python models/product_model.py
```

### **7️⃣ Run the Application**
```sh
streamlit run app.py
```

---

## 🚀 Features
✅ **Automated Sales Conversations** – AI-powered chatbot for real-time interaction.  
✅ **Product Inquiry & Search** – Users can ask about products, specifications, and pricing.  
✅ **Knowledge Retrieval System** – Fetches details from a structured product database.  
✅ **Real-time Web Search** – Uses **DuckDuckGo** for additional product insights.  
✅ **Lead Generation** – Captures customer inquiries for follow-ups.  
✅ **Scalable & Maintainable** – Built using **Python, OpenAI, Streamlit, and SQLAlchemy**.  

---

## 📊 Future Enhancements
🚀 **Vector Search** – Implement **FAISS** for advanced product retrieval.  
🎤 **Voice Support** – Add **speech-to-text** for voice-based interactions.  
📊 **Analytics Dashboard** – Track sales inquiries and chatbot performance.  
🛍️ **E-commerce Integration** – Connect with **shopping platforms** for direct purchases.  

---

## 🤝 Contribution
If you'd like to contribute:
1. **Fork** the repository.
2. **Create a new branch**: `git checkout -b feature-branch`.
3. **Commit changes**: `git commit -m 'Add new feature'`.
4. **Push to GitHub**: `git push origin feature-branch`.
5. **Open a Pull Request**.

---

## 📜 License
This project is licensed under the **MIT License** – feel free to modify and use it! 🎉

