#Projeto usando LlamaIndex com Groq
# Instalacao pip install llama_index.llms.groq

from dotenv import load_dotenv
import os
from groq import Groq
from llama_index.llms.groq import Groq

#Carrega chave
load_dotenv()

# Create the Groq client
GROQ_API = os.environ.get("GROQ_API_KEY")

llm = Groq(model='llama3-70b-8192', api_key=GROQ_API)

#response = llm.complete('Qual é a substância que dá o aroma do alecrim?')
response = llm.complete('Qual a diferença entre llamaindex, llama e groq')

paragrafos = response.text.split("\n\n")
for paragrafo in paragrafos:
    print(paragrafo)
    print()