

from dotenv import load_dotenv
load_dotenv()

from langchain import hub

from langchain_core.tools import Tool
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

from langchain.agents import AgentExecutor, create_react_agent


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

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

llm = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct", temperature=0.1)
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm = llm, tools = tools, prompt = prompt)

agent_executor = AgentExecutor.from_agent_and_tools(agent = agent, 
                                                    tools = tools,
                                                    verbose = True, 
                                                    handling_parsing_errors = True)

resp = agent_executor.invoke({"input": "Em que dia estamos?"})

resp = agent_executor.invoke({"input": "Qual a população de Paris?"})
print(resp)
