from models import db
from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from fastapi import Depends
from jose import jwt, JWTError  
from main import SECRET_KEY, ALGORITHM, oauth2_schema
def open_section():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session

    finally:
    
        session.close()
        
def verificar_token(token: str  = Depends(oauth2_schema), session: Session = Depends(open_section)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado")
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario não encontrado.")
    return usuario