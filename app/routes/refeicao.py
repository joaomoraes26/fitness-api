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