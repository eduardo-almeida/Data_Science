import os

from decouple import config

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings


os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')


if __name__ == '__main__':
    file_path = '/app/rag/data/tudo.txt'
    loader = TextLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    chunks = text_splitter.split_documents(
        documents=docs,
    )

    persist_directory = '/app/chroma_data'

    embedding = HuggingFaceEmbeddings()
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )
    vector_store.add_documents(
        documents=chunks,
    )
