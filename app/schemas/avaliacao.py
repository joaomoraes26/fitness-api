from pydantic import BaseModel 
from datetime import date

class AvaliacaoCreate(BaseModel):
    peso : float 
    altura : float 
    objetivo : str

class AvaliacaoResponse(BaseModel):
    id : int 
    usuario_id : int 
    peso : float 
    altura : float
    imc : float 
    objetivo : str
    recomendacao_texto : str 
    data : date