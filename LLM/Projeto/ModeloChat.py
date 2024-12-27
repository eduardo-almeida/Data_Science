from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from langchain_community.llms import HuggingFaceEndpoint

from langchain_openai import ChatOpenAI

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

llm = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct", temperature=0.1)
resp = llm.invoke([HumanMessage(content = "Olá! Tudo bem?")])

print(resp)