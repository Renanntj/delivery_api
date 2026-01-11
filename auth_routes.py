from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependences import open_section
from main import bcrypt_context, ALGORITHM, ACCESS_TOKEN_MINUTES, SECRET_KEY
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario):
    data_expiração = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_MINUTES)
    dic_info = {"sub": id_usuario, "exp": data_expiração}
    jwt_cod = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_cod

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario
    
@auth_router.get("/")
async def home():
    return {"resul": "ok"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session =Depends(open_section)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail='Já existe esse email')
    else:
        senha_segura = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_segura, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {f'Usuario criado com sucesso: {usuario_schema.email}'}

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session : Session = Depends(open_section)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=401, detail='Email ou Senha invalidos.')
    else:
        access_token = criar_token(usuario.id)
        return {"access_token": access_token,
                "token_type": "Bearer"
                }

