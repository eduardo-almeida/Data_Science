print("ola mundo")

import torch
from langchain_huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceHub


from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceHub(
      repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
      model_kwargs={
          "temperature": 0.1,
          "return_full_text": False,
          "max_new_tokens": 512,
          #"stop": ["<|eot_id|>"],
          # demais parâmetros que desejar
      }
  )

system_prompt = "Você é um assistente prestativo e está respondendo perguntas gerais."
user_prompt = "{input}"

token_s, token_e = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>", "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

prompt = ChatPromptTemplate.from_messages([
    ("system", token_s + system_prompt),
    ("user", user_prompt + token_e)
])

chain = prompt | llm

input = "Explique para mim em até 1 parágrafo o conceito de redes neurais, de forma clara e objetiva"

res = chain.invoke({"input": input})
print(res)
print("-----")
