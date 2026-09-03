from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from app.database import Base



class Execucao(Base):
    __tablename__ = "execucao"


    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False, index=True)
    exercicio_id = Column(Integer, ForeignKey("exercicio.id"), nullable=False, index=True)
    treino_id = Column(Integer, ForeignKey("treino.id"), index=True)
    series = Column(Integer, nullable=False)
    repeticoes = Column(Integer, nullable=False)
    carga = Column(Float)
    data = Column(Date)