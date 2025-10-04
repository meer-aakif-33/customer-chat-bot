import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from pathlib import Path

load_dotenv()

# Gemini config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-lite")

# LLM
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    api_key=GEMINI_API_KEY,
    convert_system_message_to_human=True
)

# Embeddings + FAISS
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

# Utility function to check if FAISS index exists
def kb_exists() -> bool:
    return Path(vectordb_file_path).exists()
