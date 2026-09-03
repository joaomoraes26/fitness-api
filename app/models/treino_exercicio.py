from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base



class Treino_Exercicio(Base):
    __tablename__ = "treino_exercicio"

    
    id = Column(Integer, primary_key=True, index=True)
    treino_id = Column(Integer, ForeignKey("treino.id"), nullable=False, index=True)
    exercicio_id = Column(Integer, ForeignKey("exercicio.id"), nullable=False, index=True)
    ordem = Column(Integer)
