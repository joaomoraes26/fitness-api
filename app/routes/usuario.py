from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioLogin
from app.schemas.token import TokenResponse
from app.auth import hash_senha, verificar_senha, criar_token, usuario_atual
from fastapi.security import OAuth2PasswordBearer


router = APIRouter()

@router.post("/usuarios", response_model = UsuarioResponse)
def criar_usuario(usuario : UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = Usuario(nome = usuario.nome , email = usuario.email, senha_hash = hash_senha(usuario.senha))

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario
    

@router.post("/login", response_model = TokenResponse)
def login(dados: UsuarioLogin, db: Session = Depends(get_db)):
    usuario_encontrado = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if usuario_encontrado is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    
    if not verificar_senha(dados.senha, usuario_encontrado.senha_hash):
        raise HTTPException(status_code=404, detail="Senha Incorreta")

    token = criar_token({"sub": str(usuario_encontrado.id)})
    return TokenResponse(access_token=token, token_type="bearer")


@router.get("/usuarios/me", response_model = UsuarioResponse)
def obter_perfil( db: Session = Depends(get_db), usuario_id: str = Depends(usuario_atual)):
    usuario_encontrado = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    return usuario_encontrado

