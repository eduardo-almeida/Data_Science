from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms import huggingface_hub
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv

load_dotenv()

# Exemplo com Hugging Face
llm = ChatOllama(
    model="phi3",
    temperature=0.1
)




system_prompt = "Você é um assistente prestativo e está respondendo perguntas gerais."
user_prompt = "{input}"


## llama 3
token_s, token_e = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>", "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

prompt = ChatPromptTemplate.from_messages([
    ("system", token_s + system_prompt),
    ("user", user_prompt + token_e)
])

# chain = prompt | llm

input = "Explique para mim em até 1 parágrafo o conceito de redes neurais, de forma clara e objetiva"

# res = chain.invoke({"input": input})
chain3 = prompt | llm
res = chain3.invoke({"input": input})
print(res.content)