import os
import io
import getpass
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.llms import HuggingFaceHub
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

from dotenv import load_dotenv
load_dotenv()

print("lalalalal")

video_loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=JPFNtBOrcRw",
                                              language = ["pt", "pt-BR", "en"],)

infos = video_loader.load()
transcricao = infos[0].page_content

with io.open("transcricao.txt", "w", encoding="utf-8") as f:
    for doc in infos:
        f.write(transcricao)

def model_hf_hub(model = "meta-llama/Meta-Llama-3-8B-Instruct", temperature = 0.1):
    llm = HuggingFaceHub(repo_id = model,
                        model_kwargs={
                            "temperature": temperature,
                            "return_full_text": False,
                            "max_new_tokens": 1024,
                        })
    return llm

def model_openai(model = "gpt-4o-mini", temperature = 0.1):
    llm = ChatOpenAI(model = model, temperature = temperature)
    return llm

# def model_ollama(model = "phi3", temperature = 0.1):
#     llm = ChatOllama(model = model, temperature = temperature)
#     return llm

llm = model_hf_hub()

system_prompt = "Você é um assistente virtual prestativo e deve responder a uma consulta com base na transcrição de um vídeo, que será fornecida abaixo."

inputs = "Consulta: {consulta} \n Transcrição: {transcricao}"

user_prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>".format(inputs)

prompt_template = ChatPromptTemplate.from_messages([("system", system_prompt), ("user", user_prompt)])

chain = prompt_template | llm | StrOutputParser()
# res = chain.invoke({"transcricao": transcricao, "consulta": "resuma"})

# res = chain.invoke({"transcricao": transcricao, "consulta": "sumarize de forma clara de entender"})

# res = chain.invoke({"transcricao": transcricao, "consulta": "explique em 1 frase sobre o que fala esse vídeo"})

# res = chain.invoke({"transcricao": transcricao, "consulta": "liste os temas desse video"})
# print(res)
# print("=======================================================")

# url_video = "https://www.youtube.com/watch?v=II28i__Tf3M"

# video_loader = YoutubeLoader.from_youtube_url(
#     url_video,
#     language=["pt", "en"],
#     translation="fr",
# )

# infos = video_loader.load()
# transcricao = infos[0].page_content

def llm_chain():
    system_prompt = "Você é um assistente virtual prestativo e deve responder a uma consulta com base na transcrição de um vídeo, que será fornecida abaixo."

    inputs = "Consulta: {consulta} \n Transcrição: {transcricao}"

    user_prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>".format(inputs)
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])

    llm = model_hf_hub()

    chain = prompt_template | llm | StrOutputParser()

    return chain

def get_video_info(url_video, language="pt", translation=None):

  video_loader = YoutubeLoader.from_youtube_url(
      url_video,
      language=language,
      translation=translation,
  )

  transcript = infos.page_content

  return transcript

def interpret_video(url, query="resuma", model_class="hf_hub", language="pt", translation=None):

    try:
        transcript, metadata = get_video_info(url, language, translation)

        chain = llm_chain(model_class)

        res = chain.invoke({"transcricao": transcript, "consulta": query})
        print(res)

    except Exception as e:
        print("Erro ao carregar transcrição")
        print(e)

print(transcricao)