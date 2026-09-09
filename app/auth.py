import os 
from passlib.context import CryptContext 
from jose import jwt 
from datetime import datetime, timedelta 
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool: 
    return pwd_context.verify(senha, senha_hash)

def criar_token(dados: dict):
    tempo_expirar = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados["exp"] = tempo_expirar
    
    return jwt.encode(dados, SECRET_KEY, algorithm = ALGORITHM)