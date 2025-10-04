import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from config import instructor_embeddings, vectordb_file_path
from pathlib import Path
from config import vectordb_file_path

def create_vector_db():
    st.info("Creating FAISS knowledge base...")
    loader = CSVLoader(
        file_path="dataset/dataset.csv",  # adjust path
        source_column="prompt"
    )
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)
    st.success("Knowledge base created!")

def load_vector_db():
    # Convert to Path object
    vectordb_path = Path(vectordb_file_path)

    if not vectordb_path.exists():
        create_vector_db()

    vectordb = FAISS.load_local(
        vectordb_path,
        instructor_embeddings,
        allow_dangerous_deserialization=True
    )
    return vectordb
