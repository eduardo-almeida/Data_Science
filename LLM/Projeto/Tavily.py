from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(max_results=2)

search_results = search.invoke("Qual melhor personagem do anime Dungein meshi?")
print(search_results[0]['content'])