from google import genai
from dotenv import load_dotenv

load_dotenv()

MODELO = "gemini-3.5-flash-lite"
client = genai.Client()

def perguntar(pergunta : str ) -> str:
    resposta =  client.models.generate_content(model = MODELO, contents= pergunta)
    return resposta.text
