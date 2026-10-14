from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import usuario_atual
from app.database import get_db
from app.models.refeicao import Refeicao 
from app.schemas.refeicao import RefeicaoCreate, RefeicaoResponse
from typing import List

router = APIRouter()

@router.post("/refeicoes", response_model= RefeicaoResponse)
def criar_refeicao (refeicao : RefeicaoCreate, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    cria_refeicao = Refeicao(tipo_refeicao = refeicao.tipo_refeicao, descricao_original = refeicao.descricao_original, data = refeicao.data, usuario_id = usuario_id)

    db.add(cria_refeicao)
    db.commit()
    db.refresh(cria_refeicao)

    return cria_refeicao 

@router.get("/refeicoes", response_model = List[RefeicaoResponse])
def listar_refeicoes(db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    lista_refeicoes = db.query(Refeicao).filter(Refeicao.usuario_id == usuario_id).all()
    return lista_refeicoes

@router.get("/refeicoes/{refeicao_id}", response_model= RefeicaoResponse)
def buscar_refeicao(refeicao_id : int, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    busca_refeicao = db.query(Refeicao).filter(Refeicao.id == refeicao_id, Refeicao.usuario_id == usuario_id).first()
    if busca_refeicao is None : 
        raise HTTPException (status_code= 404, detail= "Refeição não encontrada ou inexistente!")
    return busca_refeicao

