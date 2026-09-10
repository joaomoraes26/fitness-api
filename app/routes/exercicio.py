from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.exercicio import Exercicio
from app.schemas.exercicio import ExercicioCreate, ExercicioResponse
from app.auth import usuario_atual 


router = APIRouter()

@router.post("/exercicios", response_model = ExercicioResponse)
def criar_exercicio(exercicio : ExercicioCreate, db: Session = Depends(get_db), usuario_id: str = Depends(usuario_atual)):
    novo_exercicio = Exercicio(nome = exercicio.nome, grupo_muscular = exercicio.grupo_muscular, usuario_id = usuario_id)

    db.add(novo_exercicio)
    db.commit()
    db.refresh(novo_exercicio)

    return novo_exercicio