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

@router.get("/execucoes/{execucao_id}", response_model = ExecucaoResponse)
def buscar_execucao(execucao_id : int, db: Session = Depends(get_db), usuario_id : str = Depends(usuario_atual)):
    busca_execucao = db.query(Execucao).filter(Execucao.id == execucao_id, Execucao.usuario_id == usuario_id).first()
    if busca_execucao is None:
        raise HTTPException(status_code = 404, detail="Execucão não encontrada")
    return busca_execucao

@router.put("/execucoes/{execucao_id}", response_model = ExecucaoResponse)
def editar_execucao(execucao_editada : ExecucaoCreate, execucao_id : int, db:Session = Depends(get_db), usuario_id: str = Depends(usuario_atual)):
    busca_exercicio = db.query(Exercicio).filter(Exercicio.id == execucao_editada.exercicio_id, Exercicio.usuario_id == usuario_id).first()
    if busca_exercicio is None:
        raise HTTPException(status_code=404, detail= "Exercicio não encontrado")
    edita_execucao = db.query(Execucao).filter(Execucao.id == execucao_id, Execucao.usuario_id == usuario_id).first()
    if edita_execucao is None:
        raise HTTPException(status_code= 404, detail = "Execucão não encontrada")
    if execucao_editada.treino_id is not None:
        busca_treino = db.query(Treino).filter(Treino.id == execucao_editada.treino_id, Treino.usuario_id == usuario_id).first()
        if busca_treino is None: 
            raise HTTPException(status_code= 404, detail="Treino não encontrado")
    edita_execucao.series = execucao_editada.series
    edita_execucao.repeticoes = execucao_editada.repeticoes
    edita_execucao.carga = execucao_editada.carga
    edita_execucao.treino_id = execucao_editada.treino_id
    edita_execucao.exercicio_id = execucao_editada.exercicio_id
    

    db.add(edita_execucao)
    db.commit()
    db.refresh(edita_execucao)
    
    return edita_execucao