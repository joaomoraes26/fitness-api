from pydantic import BaseModel 
from typing import Optional
from datetime import date

class RefeicaoCreate(BaseModel):
    tipo_refeicao : str
    descricao_original : str
    data : date

class RefeicaoResponse(BaseModel):
    id : int 
    usuario_id : int 
    tipo_refeicao : str
    descricao_original : str
    calorias : Optional[float] = None
    proteina : Optional[float] = None
    carboidrato : Optional[float] = None
    gordura : Optional[float] = None
    data : date