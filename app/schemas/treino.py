from pydantic import BaseModel 

class TreinoCreate(BaseModel):
   nome: str

class TreinoResponse(BaseModel):
   id: int
   usuario_id: int
   nome: str 
