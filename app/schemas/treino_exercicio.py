from pydantic import BaseModel
from typing import Optional

class TreinoExercicioCreate(BaseModel):
    treino_id: int 
    exercicio_id: int 

class TreinoExercicioResponse(BaseModel):
    id: int
    treino_id: int
    exercicio_id: int 
    ordem: Optional[int] = None