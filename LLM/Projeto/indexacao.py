import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate

from langchain_text_splitters import RecursiveCharacterTextSplitter

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

from dotenv import load_dotenv
load_dotenv()

loader = WebBaseLoader(web_paths = ("https://www.bbc.com/portuguese/articles/cd19vexw0y1o",),)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200, add_start_index = True)
splits = text_splitter.split_documents(docs)

hf_embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2")

input_test = "Um teste apenas"
result = hf_embeddings.embed_query(input_test)

vectorstore = Chroma.from_documents(documents=splits, embedding=hf_embeddings)
retriever = vectorstore.as_retriever(search_type = "similarity", search_kwargs={"k": 6})


template_rag = """
<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
Você é um assistente virtual prestativo e está respondendo perguntas gerais.
Use os seguintes pedaços de contexto recuperado para responder à pergunta.
Se você não sabe a resposta, apenas diga que não sabe. Mantenha a resposta concisa.
<|eot_id|>
<|start_header_id|>user<|end_header_id|>
Pergunta: {pergunta}
Contexto: {contexto}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

prompt_rag = PromptTemplate(
    input_variables=["contexto", "pergunta"],
    template=template_rag,
)

def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)

llm = HuggingFaceHub(
      repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
      model_kwargs={
          "temperature": 0.1,
          "return_full_text": False,
          "max_new_tokens": 512,
      }
  )

chain_rag = ({"contexto": retriever | format_docs, "pergunta": RunnablePassthrough()}
             | prompt_rag
             | llm
             | StrOutputParser())

res = chain_rag.invoke("Qual filme ganhou mais oscars na premiação de 2024?")

print(res)

vectorstore.delete_collection()