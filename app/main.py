from fastapi import FastAPI
from app.database import Base, engine 
from app.routes import usuario, exercicio, treino , treino_exercicio, execucao
import app.models 

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(usuario.router)
app.include_router(exercicio.router)
app.include_router(treino.router)
app.include_router(treino_exercicio.router)
app.include_router(execucao.router)

@app.get("/")
def read_root():
    return {"mensagem": "API Fitness funcionando!"}