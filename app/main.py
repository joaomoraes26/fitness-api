from fastapi import FastAPI
from app.database import Base, engine 
import app.models 



Base.metadata.create_all(bind=engine)



app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API Fitness funcionando!"}