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

from langchain.globals import set_debug
set_debug(True)

llm = HuggingFaceHub(
      repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
      model_kwargs={
          "temperature": 0.1,
          "return_full_text": False,
          "max_new_tokens": 512,
      }
  )


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


chain_rag = prompt_rag | llm | StrOutputParser()
contexto = """Faturamento trimestral:
1º: R$42476,40
2º: R$46212,97
3º: R$41324,56
4º: R$56430,24"""

#pergunta = "Qual é o faturamento do segundo trimestre?"
pergunta = "Qual trimestre teve o menor faturamento?"

res = chain_rag.invoke({
  "contexto": contexto,
  "pergunta": pergunta
})

print(res)