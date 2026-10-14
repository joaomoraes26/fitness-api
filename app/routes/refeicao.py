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

@router.put("/refeicoes/{refeicao_id}", response_model= RefeicaoResponse)
def editar_refeicao(refeicao_editada : RefeicaoCreate, refeicao_id : int, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    busca_refeicao = db.query(Refeicao).filter(Refeicao.id == refeicao_id, Refeicao.usuario_id == usuario_id).first()
    if busca_refeicao is None: 
        raise HTTPException (status_code= 404, detail= "Refeição não encontrada!")
    if busca_refeicao.descricao_original != refeicao_editada.descricao_original:
        busca_refeicao.calorias = None
        busca_refeicao.gordura = None
        busca_refeicao.proteina = None
        busca_refeicao.carboidrato = None

    busca_refeicao.tipo_refeicao = refeicao_editada.tipo_refeicao
    busca_refeicao.descricao_original = refeicao_editada.descricao_original
    busca_refeicao.data = refeicao_editada.data

    db.add(busca_refeicao)
    db.commit()
    db.refresh(busca_refeicao)

    return busca_refeicao


@router.delete("/refeicoes/{refeicao_id}")
def deletar_refeicao(refeicao_id : int, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    deleta_refeicao = db.query(Refeicao).filter(Refeicao.id == refeicao_id, Refeicao.usuario_id == usuario_id).first()
    if deleta_refeicao is None:
        raise HTTPException (status_code= 404, detail= "Refeição não encontrada!")

    db.delete(deleta_refeicao)
    db.commit()

    return {"detail" : "Refeição deletada com sucesso!"}