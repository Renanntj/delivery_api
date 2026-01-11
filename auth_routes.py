from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependences import open_section
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

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
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, usuario_schema.ativo, usuario_schema.admin, senha_segura)
        session.add(novo_usuario)
        session.commit()
        return HTTPException(status_code=201, detail=f'Usuario criado com sucesso: {usuario_schema.email}')

