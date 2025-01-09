import torch
import os
import getpass

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline
from langchain_community.llms import HuggingFaceHub
from langchain_core.messages import HumanMessage

from langchain.prompts import PromptTemplate
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langgraph.prebuilt import create_react_agent as langgraph_react_agent
from langchain_core.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

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

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=3000))
wikipedia_tool = Tool(name = "wikipedia",
                      description="You must never search for multiple concepts at a single step, you need to search one at a time. When asked to compare two concepts for example, search for each one individually.",
                      func=wikipedia.run)

def current_day(*args, **kwargs):
  from datetime import date

  dia = date.today()
  dia = dia.strftime('%d/%m/%Y')
  return dia

date_tool = Tool(name="Day", func = current_day,
                 description = "Use when you need to know the current date")

tools = [wikipedia_tool, date_tool]


from datetime import date
agent_executor = langgraph_react_agent(llm, tools)
input = "Qual é o valor de mercado recente da NVIDIA?"

response = agent_executor.invoke({"messages": [HumanMessage(content=input)]})
response["messages"]
print(response)
#defeito