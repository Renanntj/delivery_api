from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType
db = create_engine("sqlite:///banco.db")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=True)
    
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"
    
    # STATUS_PEDIDOS = (
    #     (1, "PENDENTE"),
    #     (2, "FINALIZADO"),
    #     (3, "CANCELADO")  
    # )
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    status = Column("status",String) # pendente cancelado finzalizado 
    
    def __init__(self, usuario, preco=0, status=1):
        self.usuario = usuario
        self.preco = preco
        self.status = status    
    
class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    # TAMANHO_PEDIDOS = (
        
    #     (1, 'P'),
    #     (2, 'M'),
    #     (3, 'G')        
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade =  Column(Integer)
    sabor = Column(String)
    tamanho = Column(String)
    preco_uni  = Column(Float)
    pedido = Column(ForeignKey("pedidos.id"))
    
    def __init__(self, quantidade, sabor, tamanho, preco_uni, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_uni = preco_uni
        self.pedido = pedido
   
   