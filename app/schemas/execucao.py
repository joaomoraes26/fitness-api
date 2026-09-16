from pydantic import BaseModel
from typing import Optional
from datetime import date

class ExecucaoCreate(BaseModel):
    exercicio_id : int 
    treino_id: Optional[int] = None
    series: int 
    repeticoes: int 
    carga: Optional[float] = None

class ExecucaoResponse(BaseModel):
    id: int
    usuario_id: int
    exercicio_id : int 
    treino_id: Optional[int] = None
    series: int 
    repeticoes: int 
    carga: Optional[float] = None
    data: date 