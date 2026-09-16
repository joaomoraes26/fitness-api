from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.execucao import Execucao
from app.models.exercicio import Exercicio
from app.models.treino import Treino
from app.schemas.execucao import ExecucaoCreate, ExecucaoResponse
from app.auth import usuario_atual 
from datetime import date

router = APIRouter()


@router.post("/execucoes", response_model= ExecucaoResponse)
def criar_execucao(execucao : ExecucaoCreate, db: Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    busca_exercicio = db.query(Exercicio).filter(Exercicio.id == execucao.exercicio_id, Exercicio.usuario_id == usuario_id).first()
    if busca_exercicio is None:
        raise HTTPException(status_code=404, detail= "Exercicio não encontrado")
    if execucao.treino_id is not None:
        busca_treino = db.query(Treino).filter(Treino.id == execucao.treino_id, Treino.usuario_id == usuario_id).first()
        if busca_treino is None:
            raise HTTPException(status_code=404, detail="Treino não encontrado")
    data_hoje = date.today()
    cria_execucao = Execucao(usuario_id = usuario_id, exercicio_id = execucao.exercicio_id, treino_id = execucao.treino_id, series = execucao.series, repeticoes = execucao.repeticoes, carga = execucao.carga, data = data_hoje)

    db.add(cria_execucao)
    db.commit()
    db.refresh(cria_execucao)

    return cria_execucao

@router.get("/execucoes", response_model = List[ExecucaoResponse])
def listar_execucoes(db:Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    lista_execucoes = db.query(Execucao).filter(Execucao.usuario_id == usuario_id).all()
    return lista_execucoes