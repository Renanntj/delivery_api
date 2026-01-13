from fastapi import APIRouter, Depends, HTTPException
from dependences import open_section, verificar_token
from sqlalchemy.orm import Session
from schemas import PedidoSchema, ItemPedidoSchema, PedidoRespondeSchema
from models import Pedido, Usuario, ItemPedido
from typing import List

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@order_router.post("/pedido")
async def pedido(pedido_schema:PedidoSchema, session: Session = Depends(open_section)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso! ID: {novo_pedido.id}"}

@order_router.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Permissão negada")
    
    pedido.status = "Cancelado"
    session.commit()
    return {
        "mensagem": f"Pedido {pedido.id} cancelado com sucesso.",
        "pedido": pedido
    }


#só admin
@order_router.get("/listar")
async def listar_pedido(session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Acesso Negado")
    else:
        pedidos = session.query(Pedido).all()
    return {
        "pedido" : pedidos
    }
    
@order_router.post("/pedido/adicionar-item/{id_pedido}")
async def add_pedido(id_pedido: int,item_schema: ItemPedidoSchema, session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id !=  pedido.usuario:
        raise HTTPException(status_code=401, detail="Acesso Negado.")
    item_pedido = ItemPedido(item_schema.quantidade, item_schema.sabor, item_schema.tamanho, item_schema.preco_uni, id_pedido)
    session.add(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return {
        "mensagem": "Pedido adicionado com sucesso",
        "item_id": item_pedido.id,
        "preco": pedido.preco
    }

@order_router.post("/pedido/remover-item/{id_item_pedido}")
async def dell_pedido(id_item_pedido: int,session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    item_pedido = session.query(ItemPedido).filter(Pedido.id==id_item_pedido).first()
    pedido = session.query(Pedido).filter(Pedido.id==id_item_pedido).first()
    if not item_pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Acesso Negado.")
    session.delete(item_pedido)
    pedido.calcular_preco()
    session.commit()
    return {
        "mensagem": "Pedido deletado com sucesso",
        "quantidades_itens_pedido": len(pedido.itens),
        "pedido": pedido
    }
    
    

@order_router.post("/pedido/finalizar/{id_pedido}")
async def finalizar_pedido(id_pedido: int, session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Permissão negada")
    
    pedido.status = "Finalizado"
    session.commit()
    return {
        "mensagem": f"Pedido {pedido.id} finalizado com sucesso.",
        "pedido": pedido
    }
    


@order_router.get("/pedidos/pedidos-usuarios", response_model=List[PedidoRespondeSchema])
async def listar_pedidos_usuario(session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    pedidos = session.query(Pedido).filter(Pedido.usuario==usuario.id).all()
    return pedidos

@order_router.get("/pedido/{id_pedido}")
async def listar_pedido(id_pedido: int, session: Session = Depends(open_section), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Acesso Negado.")
    return {
        "quantidade_itens_pedido": len(pedido.itens),
        "pedido": pedido
    }


    