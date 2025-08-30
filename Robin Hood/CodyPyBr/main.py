import os
import json

# from decouple import config
from pprint import pprint
# from bot.ai_bot import AIBot

from langchain_groq import ChatGroq
from langchain.chains import create_extraction_chain
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# ai_bot = AIBot()
llm = ChatGroq(model='llama-3.3-70b-versatile')

# schema = {
#     'properties': {
#         'posicao': {'type': 'integer'},
#         'time': {'type': 'string'},
#         'jogos': {'type': 'integer'},
#         'vitorias': {'type': 'integer'},
#         'empates': {'type': 'integer'},
#         'derrotas': {'type': 'integer'},
#         'gols_pro': {'type': 'integer'},
#         'gols_contra': {'type': 'integer'},
#         'saldo_gols': {'type': 'integer'},
#         'pontos': {'type': 'integer'},
#     },
# }

schema = {
    'properties': {
        'data': {'type': 'string'}, 
        'time1': {'type': 'string'},
        'time2': {'type': 'string'},
        '1': {'type': 'float'},
        'x': {'type': 'float'},
        '2': {'type': 'float'},
    },
}

def extract(content: str, schema: dict):
    return create_extraction_chain(
        schema=schema,
        llm=llm,
    ).invoke(content).get('text')

def scrape_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        documents=docs,
        tags_to_extract=['table'],
    )
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000,
        chunk_overlap=0,
    )
    splits = splitter.split_documents(
        documents=docs_transformed,
    )
    extracted_content = []

    for split in splits:
        extracted_content.extend(
            extract(
                schema=schema,
                content=split.page_content,
            )
        )
    return extracted_content


if __name__ == '__main__':
    # urls = ['https://ge.globo.com/futebol/brasileirao-serie-a/']
    urls = ['https://https://bullsbet.bet.br/sports?leagueId=677879777860075520']
    extracted_content = scrape_with_playwright(
        urls=urls,
        schema=schema,
    )
    pprint(
        object=extracted_content,
        indent=4,
        sort_dicts=False,
    )
    with open('data.json', 'w') as fp:
        json.dump(
            obj=extracted_content, 
            fp=fp,
            ensure_ascii=False,
            indent=4,
        )
