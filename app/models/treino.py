from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base



class Treino(Base):
    __tablename__ = "treino"

    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"),nullable=False, index=True)
    nome = Column(String(100), nullable=False)