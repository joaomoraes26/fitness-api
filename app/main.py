from fastapi import FastAPI
from app.database import Base, engine 
from app.routes import usuario
import app.models 

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(usuario.router)


@app.get("/")
def read_root():
    return {"mensagem": "API Fitness funcionando!"}