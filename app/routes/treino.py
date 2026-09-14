from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.treino import Treino
from app.schemas.treino import TreinoCreate, TreinoResponse
from app.auth import usuario_atual 

router = APIRouter() 

@router.post("/treinos", response_model= TreinoResponse)
def criar_treino(treino: TreinoCreate, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    novo_treino = Treino(nome = treino.nome, usuario_id = usuario_id)

    db.add(novo_treino)
    db.commit()
    db.refresh(novo_treino)

    return novo_treino

@router.get("/treinos", response_model= List[TreinoResponse])
def listar_treino(db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    lista_treino = db.query(Treino).filter(Treino.usuario_id == usuario_id).all()
    return lista_treino

@router.get("/treinos/{treino_id}", response_model= TreinoResponse)
def buscar_treino(treino_id: int, db : Session = Depends(get_db), usuario_id: str = Depends(usuario_atual)):
    busca_treino = db.query(Treino).filter(Treino.id == treino_id, Treino.usuario_id == usuario_id).first()
    if busca_treino is None:
        raise HTTPException(status_code=404, detail="Treino não encontrado")
    return busca_treino

@router.put("/treinos/{treino_id}", response_model = TreinoResponse)
def editar_treino(treino_editado : TreinoCreate, treino_id: int, db: Session = Depends(get_db), usuario_id :str = Depends(usuario_atual)):
    edita_treino = db.query(Treino).filter(Treino.id == treino_id, Treino.usuario_id == usuario_id).first()
    if edita_treino is None:
        raise HTTPException(status_code=404, detail="Treino não encontrado")
    edita_treino.nome = treino_editado.nome

    db.add(edita_treino)
    db.commit()
    db.refresh(edita_treino)

    return edita_treino

@router.delete("/treinos/{treino_id}")
def deletar_treino(treino_id: int, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    deleta_treino = db.query(Treino).filter(Treino.id == treino_id, Treino.usuario_id == usuario_id).first()
    if deleta_treino is None:
        raise HTTPException (status_code=404, detail= "Treino não encontrado")

    db.delete(deleta_treino)
    db.commit()

    return{"detail" : "Treino deletado com sucesso"}