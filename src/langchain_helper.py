import os
from dotenv import load_dotenv
import time
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, ServiceUnavailable

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

# Configure Gemini SDK
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create LangChain LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

# Embeddings
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path="C:/Users/ADMIN/Desktop/VS_Code/GEN---AI-course/GEN---AI-course/customer_service_chatbot_LLM/dataset/dataset.csv", source_column="prompt")
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer, use as much text as possible from the "response" section in the source document.
    If the answer is not found in the context, say "I don't know."

    CONTEXT: {context}
    QUESTION: {question}"""

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT},
    )

def generate_with_retry(model_name, prompt, max_retries=5, initial_delay=1, max_delay=60):
    delay = initial_delay
    model = genai.GenerativeModel(model_name)
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except (ResourceExhausted, ServiceUnavailable) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay = min(delay * 2, max_delay)
            else:
                print("Max retries reached. Returning None.")
                return None

# Example usage
if __name__ == "__main__":
    create_vector_db()
    chain = get_qa_chain()
    print(chain.invoke({"query": "I have never done programming in my life. Can I take this course?"}))
    
    result = generate_with_retry("gemini-1.5-flash", "Hello, tell me a story about a cat.")
    print("Generated content:", result)
