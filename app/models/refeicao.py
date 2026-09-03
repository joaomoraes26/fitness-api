from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from app.database import Base



class Refeicao(Base): 
    __tablename__ = "refeicao"


    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False, index=True)
    tipo_refeicao = Column(String(255), nullable=False)
    descricao_original = Column(String(255), nullable=False)
    calorias = Column(Float)
    proteina = Column(Float)
    carboidrato = Column(Float)
    gordura = Column(Float)
    data = Column(Date)