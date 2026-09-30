from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import usuario_atual 
from datetime import date
from app.database import get_db
from app.models.avaliacao import Avaliacao
from app.schemas.avaliacao import AvaliacaoCreate, AvaliacaoResponse

router = APIRouter()

@router.post("/avaliacoes" , response_model= AvaliacaoResponse)
def criar_avaliacao (avaliacao : AvaliacaoCreate, db : Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    imc_calculado = avaliacao.peso/ (avaliacao.altura ** 2) 
    if imc_calculado < 18.5:
        recomendacao =  "Abaixo do Peso!"
    elif imc_calculado < 25: 
        recomendacao = " Peso dentro do esperado!"
    else : 
        recomendacao = "Acima do peso"
    data_hoje = date.today()
    cria_avalicao = Avaliacao(peso = avaliacao.peso, altura = avaliacao.altura, objetivo = avaliacao.objetivo, imc = imc_calculado, recomendacao_texto = recomendacao, usuario_id = usuario_id, data = data_hoje)

    db.add(cria_avalicao)
    db.commit()
    db.refresh(cria_avalicao)

    return cria_avalicao