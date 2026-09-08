from fastapi import APIRouter 
from fastapi import Depends
from sqlalchemy.orm import Session 
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.auth import hash_senha




router = APIRouter()

@router.post("/usuarios", response_model = UsuarioResponse)
def criar_usuario(usuario : UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = Usuario(nome = usuario.nome , email = usuario.email, senha_hash = hash_senha(usuario.senha))

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

