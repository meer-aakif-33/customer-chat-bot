from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from config import llm
from vector_db import load_vector_db

# Load vector DB
vectordb = load_vector_db()
retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Prompt template
prompt_template = """You are a helpful assistant.
Given the following context and a question, answer using ONLY the context.
If the answer is not found in the context, say "I don't know."

CONTEXT:
{context}

QUESTION:
{question}
"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Build QA chain
chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT},
)
