from fastapi import APIRouter, Depends, HTTPException
from typing import List
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


@router.get("/exercicios", response_model = List[ExercicioResponse])
def listar_exercicio(db: Session = Depends(get_db), usuario_id: str = Depends(usuario_atual)):
    lista_exercicio = db.query(Exercicio).filter(Exercicio.usuario_id == usuario_id).all()
    return lista_exercicio


@router.get("/exercicios/{exercicio_id}", response_model = ExercicioResponse)
def buscar_exercicio(exercicio_id: int, db: Session = Depends(get_db), usuario_id:str = Depends(usuario_atual)):
    busca_exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id, Exercicio.usuario_id == usuario_id).first()
    if busca_exercicio is None:
            raise HTTPException(status_code=404, detail="Exercicio não encontrado")
    return busca_exercicio
    

@router.put("/exercicios/{exercicio_id}", response_model= ExercicioResponse)
def editar_exercicio(exercicio_editado: ExercicioCreate, exercicio_id: int, db: Session = Depends(get_db), usuario_id:str = Depends(usuario_atual)):
    busca_exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id, Exercicio.usuario_id == usuario_id).first()
    if busca_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercicio não encontrado")
    busca_exercicio.nome = exercicio_editado.nome
    busca_exercicio.grupo_muscular = exercicio_editado.grupo_muscular

    db.add(busca_exercicio)
    db.commit()
    db.refresh(busca_exercicio)

    return busca_exercicio

@router.delete("/exercicios/{exercicio_id}")
def deletar_exercicio(exercicio_id: int, db: Session = Depends(get_db), usuario_id:str = Depends(usuario_atual)):
     deleta_exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id, Exercicio.usuario_id == usuario_id).first()
     if deleta_exercicio is None:
          raise HTTPException(status_code=404, detail="Exercicio não encontrado")

     db.delete(deleta_exercicio)
     db.commit()

     return {"detail" : "Exercicio deletado com sucesso"}