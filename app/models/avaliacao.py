from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from app.database import Base



class Avaliacao(Base):
    __tablename__ = "avaliacao"


    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False, index=True)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    imc = Column(Float, nullable=False)
    objetivo = Column(String(255), nullable=False)
    recomendacao_texto = Column(String(255), nullable=False)
    data = Column(Date)

