from fastapi import APIRouter, Depends
from dependences import open_section
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Hello, world!"}

@order_router.post("/pedido")
async def pedido(pedido_schema:PedidoSchema, session: Session = Depends(open_section)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso! ID: {novo_pedido.id}"}