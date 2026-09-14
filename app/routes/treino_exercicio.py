from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.treino_exercicio import Treino_Exercicio
from app.schemas.treino_exercicio import TreinoExercicioCreate, TreinoExercicioResponse
from app.models.exercicio import Exercicio   
from app.models.treino import Treino
from app.schemas.exercicio import ExercicioResponse
from app.auth import usuario_atual 

router = APIRouter()

@router.post("/treino_exercicio", response_model= TreinoExercicioResponse)
def criar_treino_exercicio(treino_exercicio : TreinoExercicioCreate, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    treino_encontrado = db.query(Treino).filter(Treino.id == treino_exercicio.treino_id, Treino.usuario_id == usuario_id).first()
    if treino_encontrado is None:
        raise HTTPException(status_code=404, detail ="Treino não encontrado")
    exercicio_encontrado = db.query(Exercicio).filter(Exercicio.id == treino_exercicio.exercicio_id, Exercicio.usuario_id == usuario_id).first()
    if exercicio_encontrado is None:
        raise HTTPException(status_code=404 , detail= "Exercicio não encontrado")
    cria_treino_exercicio = Treino_Exercicio(treino_id = treino_encontrado.id, exercicio_id = exercicio_encontrado.id)

    db.add(cria_treino_exercicio)
    db.commit()
    db.refresh(cria_treino_exercicio)

    return cria_treino_exercicio

@router.get("/treinos/{treino_id}/exercicios", response_model= List[ExercicioResponse])
def listar_treino_exercicios(treino_id : int, db : Session = Depends(get_db), usuario_id: str = Depends(usuario_atual)):
    treino_encontrado = db.query(Treino).filter(Treino.id == treino_id, Treino.usuario_id == usuario_id).first()
    if treino_encontrado is None: 
        raise HTTPException(status_code=404, detail="Treino não encontrado") 
    lista_treino_exercicios = db.query(Exercicio).join(Treino_Exercicio, Treino_Exercicio.exercicio_id == Exercicio.id).filter(Treino_Exercicio.treino_id == treino_id).all()

    return lista_treino_exercicios