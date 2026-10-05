from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import usuario_atual 
from datetime import date
from app.database import get_db
from app.models.avaliacao import Avaliacao
from app.schemas.avaliacao import AvaliacaoCreate, AvaliacaoResponse
from typing import List
from app.recomendacao import gerar_recomendacao

router = APIRouter()

@router.post("/avaliacoes" , response_model= AvaliacaoResponse)
def criar_avaliacao (avaliacao : AvaliacaoCreate, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    imc_calculado = avaliacao.peso/ (avaliacao.altura ** 2) 
    recomendacao = gerar_recomendacao(imc_calculado, avaliacao.objetivo)
    data_hoje = date.today()
    cria_avalicao = Avaliacao(peso = avaliacao.peso, altura = avaliacao.altura, objetivo = avaliacao.objetivo, imc = imc_calculado, recomendacao_texto = recomendacao, usuario_id = usuario_id, data = data_hoje)

    db.add(cria_avalicao)
    db.commit()
    db.refresh(cria_avalicao)

    return cria_avalicao

@router.get("/avaliacoes", response_model= List[AvaliacaoResponse])
def listar_avaliacao(db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    lista_avaliacao = db.query(Avaliacao).filter(Avaliacao.usuario_id == usuario_id).all()
    return lista_avaliacao 

@router.get("/avaliacoes/{avaliacao_id}", response_model= AvaliacaoResponse)
def buscar_avaliacao(avaliacao_id : int, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    busca_avaliacao = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id, Avaliacao.usuario_id == usuario_id).first()
    if busca_avaliacao is None:
        raise HTTPException (status_code=404, detail= "Avaliação não encontrada!")
    return busca_avaliacao

@router.put("/avaliacoes/{avaliacao_id}" , response_model = AvaliacaoResponse)
def editar_avaliacao(avaliacao_editada : AvaliacaoCreate, avaliacao_id : int, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    busca_avaliacao = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id, Avaliacao.usuario_id == usuario_id).first()
    if busca_avaliacao is None:
        raise HTTPException (status_code=404, detail="Avaliação não encontrada!")
    imc_recalculado = avaliacao_editada.peso/ (avaliacao_editada.altura ** 2)
    recomendacao_nova = gerar_recomendacao(imc_recalculado, avaliacao_editada.objetivo)
    busca_avaliacao.altura = avaliacao_editada.altura
    busca_avaliacao.peso = avaliacao_editada.peso
    busca_avaliacao.imc = imc_recalculado 
    busca_avaliacao.recomendacao_texto = recomendacao_nova
    busca_avaliacao.objetivo = avaliacao_editada.objetivo
    busca_avaliacao.data = date.today()

    db.add(busca_avaliacao)
    db.commit()
    db.refresh(busca_avaliacao)

    return busca_avaliacao

@router.delete("/avaliacoes/{avaliacao_id}")
def deletar_avaliacao(avaliacao_id : int, db: Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    deleta_avaliacao = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id, Avaliacao.usuario_id == usuario_id).first()
    if deleta_avaliacao is None:
        raise HTTPException (status_code= 404, detail="Avaliação não encontrada")

    db.delete(deleta_avaliacao)
    db.commit()

    return {"detail" : " Avaliação deletada com sucesso "}

