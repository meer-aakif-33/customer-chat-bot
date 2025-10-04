---

# 🤖 Customer Service Chatbot (Gemini + FAISS)

An interactive AI-powered **Customer Service Chatbot** built with **Streamlit, LangChain, and Google Gemini API**. It enables intelligent question answering from structured datasets using **semantic search** with **FAISS** and **HuggingFace embeddings**, and provides a responsive web interface for real-time conversations.

---

## 🛠 Features

* **AI-Powered Chat:** Uses Google Gemini LLM via LangChain for context-aware responses.
* **Semantic Knowledge Retrieval:** Implements FAISS vector database with HuggingFace embeddings to search CSV datasets.
* **Real-Time Streamlit UI:** Clean, responsive interface with user/bot chat bubbles, timestamps, and chat history.
* **Knowledge Base Management:** Automatically creates a FAISS knowledge base if missing.
* **Modular Design:** Code separated into `config`, `vector_db`, `qa_chain`, and `app` for maintainability and scalability.

---

## 📂 Project Structure

```
customer_service_chatbot_LLM/
├─ dataset/
│  └─ dataset.csv          # CSV with prompts and responses
├─ src/
│  ├─ app.py               # Streamlit frontend UI
│  ├─ config.py            # API keys, model config, embeddings
│  ├─ vector_db.py         # Load/Create FAISS knowledge base
│  └─ qa_chain.py          # Prompt template & RetrievalQA chain
├─ .env                    # Gemini API key and model configuration
└─ README.md
```

---

## ⚡ Technologies Used

* **Streamlit** – Interactive web interface
* **LangChain** – LLM orchestration and QA chain
* **Google Gemini API** – Large Language Model for intelligent responses
* **FAISS** – Vector database for semantic search
* **HuggingFace Instruct Embeddings** – Embedding generation for knowledge retrieval
* **Python** – Backend scripting

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/customer_service_chatbot_LLM.git
cd customer_service_chatbot_LLM/src
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**
`streamlit`, `langchain`, `langchain-community`, `google-generativeai`, `huggingface-hub`, `faiss-cpu`, `python-dotenv`

### 3. Set up environment variables

Create a `.env` file in `src/`:

```env
GEMINI_API_KEY=your_google_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash-lite
```

### 4. Add your dataset

Ensure your `dataset/dataset.csv` has the following format:

```csv
prompt,response
I have never done programming in my life. Can I take this course?,"Yes, this is the perfect training for anyone..."
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 💡 Usage

1. Open the Streamlit app in your browser.
2. Type a question in the input box.
3. The chatbot will respond using your knowledge base.
4. The retrieved documents are viewable under **“Retrieved Context Documents”** if enabled.

---

## 🔧 Future Improvements

* Add **avatars** and auto-scroll for a ChatGPT-like experience.
* Add **multi-file knowledge base support**.
* Improve **retry logic** and caching for large datasets.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---
