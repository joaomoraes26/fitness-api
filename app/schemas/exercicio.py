from pydantic import BaseModel

class ExercicioCreate(BaseModel):
    nome: str
    grupo_muscular: str

class ExercicioResponse(BaseModel): 
    id: int 
    nome:str
    grupo_muscular: str 
    usuario_id: int 

