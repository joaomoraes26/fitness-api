from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base



class Exercicio(Base): 
    __tablename__ = "exercicio"
           

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"),nullable=False, index=True)
    nome = Column(String(255), nullable=False)
    grupo_muscular = Column(String(255), nullable=False)
            