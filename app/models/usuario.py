from sqlalchemy import Column, Integer, String 
from app.database import Base



class Usuario(Base): 
    __tablename__ = "usuario"


    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
