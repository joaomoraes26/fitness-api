import os 
from passlib.context import CryptContext 
from jose import jwt, JWTError 
from datetime import datetime, timedelta 
from dotenv import load_dotenv
from fastapi import HTTPException, Depends 
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
security = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool: 
    return pwd_context.verify(senha, senha_hash)

def criar_token(dados: dict):
    tempo_expirar = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados["exp"] = tempo_expirar
    
    return jwt.encode(dados, SECRET_KEY, algorithm = ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = payload["sub"]
        return usuario_id
    except JWTError:
        raise HTTPException(status_code=401, detail="token invalido")

def usuario_atual(credenciais: HTTPAuthorizationCredentials = Depends(security)):
    usuario_id = verificar_token(credenciais.credentials)
    return usuario_id