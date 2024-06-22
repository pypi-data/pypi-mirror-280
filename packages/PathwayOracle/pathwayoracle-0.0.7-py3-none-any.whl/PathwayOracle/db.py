# db.py

from langchain_community.graphs import Neo4jGraph
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain_community.vectorstores.neo4j_vector import Neo4jVector

from langchain.prompts.prompt import PromptTemplate
from langchain.chains import GraphCypherQAChain

import requests


OPENAI_MODEL = "gpt-3.5-turbo"

llm = None

def queryToServer(query):
    response = requests.get('https://azureflask-po.azurewebsites.net/query', params={'query': query})
    return response.json()

def cQueryToServer(query, parameters):
    response = requests.get('https://azureflask-po.azurewebsites.net/cQuery', params={'query': query, 'params':parameters})
    return response.json()

def connect_to_LLM(llm_opt):
    global llm
    try:
        print("Attempting connection with LLM ChatOpenAi")
        llm = ChatOpenAI(
            openai_api_key = llm_opt,
            model = OPENAI_MODEL,
            temperature=0.0
        )

        embeddings= OpenAIEmbeddings(
            openai_api_key=llm_opt
        )
    except:
        print("Incorrect API key")
    else:
        print('Connection successful')
        return llm
    
