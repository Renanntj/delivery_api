from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependences import open_section
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"resul": "ok"}

@auth_router.post("/criar_conta")
async def criar_conta(nome: str,email: str, senha: str, session=Depends(open_section)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        raise HTTPException(status_code=400, detail='Já existe esse email')
    else:
        senha_segura = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_segura)
        session.add(novo_usuario)
        session.commit()
        return HTTPException(status_code=201, detail=f'Usuario criado com sucesso: {email}')

