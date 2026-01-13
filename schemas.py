from pydantic import BaseModel
from typing import Optional, List

class UsuarioSchema(BaseModel):
    nome : str
    email : str
    senha : str
    ativo : Optional[bool]
    admin : Optional[bool]
    
    class Config:
        from_attributes = True
        
class LoginSchema(BaseModel):
    email : str
    senha : str
    
    class Config:
        from_attributes = True
        
class PedidoSchema(BaseModel):
    usuario : int
    
    class Config:
        from_attributes = True
        
class ItemPedidoSchema(BaseModel):
    quantidade :  int
    sabor : str
    tamanho : str
    preco_uni  : float
    
    class Config:
        from_attributes = True

class PedidoRespondeSchema(BaseModel):
    id : int
    preco : float
    status : str
    itens: List[ItemPedidoSchema]
    class Config:
        from_attributes = True