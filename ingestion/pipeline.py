from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from .summarizer import summarize_text

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)


def add_document(text: str, doc_id: str):
    vectordb.add_texts([text], ids=[doc_id])

    