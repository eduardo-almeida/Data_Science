import torch
import os
import getpass

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline
from langchain_community.llms import HuggingFaceHub

from langchain.prompts import PromptTemplate
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

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

# PHI 3
#template = """
#<|system|>
#Você é um assistente virtual prestativo e está respondendo perguntas gerais. <|end|>
#<|user|>
#{pergunta}<|end|>
#<|assistant|>
#"""

# LLAMA 3
template = """
<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
Você é um assistente virtual prestativo e está respondendo perguntas gerais.
<|eot_id|>
<|start_header_id|>user<|end_header_id|>
{pergunta}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""
prompt = PromptTemplate.from_template(template)

chain = prompt | llm

res = "Lalala"# chain.invoke({"pergunta": "Que dia é hoje?"})
print(res)
print("========================================================================")

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
prompt_rag = PromptTemplate.from_template(template_rag)

from datetime import date

dia = date.today()
contexto = "Você sabe que hoje é dia '{}'".format(dia)

chain_rag = prompt_rag | llm | StrOutputParser()

pergunta = "Que dia é hoje? Retorne a data em formato dd/mm/yyyy"

res = chain_rag.invoke({"pergunta": pergunta, "contexto": contexto})
print(res)