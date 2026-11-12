from google import genai
from dotenv import load_dotenv
from google.genai import errors

load_dotenv()

MODELO = "gemini-3.5-flash-lite"
client = genai.Client()

class IAIndisponivelError(Exception):
    pass 

def perguntar(pergunta : str ) -> str:
    try:
        resposta =  client.models.generate_content(model = MODELO, contents= pergunta)
        return resposta.text
    except errors.APIError :
        raise IAIndisponivelError("IA Indisponivel !")

def perguntar_estruturado(question : str, molde):
    conf = {"response_mime_type" : "application/json" , "response_schema" : molde }
    try: 
        answer = client.models.generate_content(model = MODELO, contents= question, config = conf)
    except errors.APIError :
        raise IAIndisponivelError("IA indisponivel")

    resultado = answer.parsed
    if resultado is None:
        raise IAIndisponivelError("Texto Incorreto")
    return resultado

