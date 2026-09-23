from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.db import SessionDep
from app.models.producto import Producto

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=Producto)
def crear_producto(producto: Producto, session: SessionDep):
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


@router.get("/", response_model=list[Producto])
def listar_productos(session: SessionDep):
    return session.exec(select(Producto)).all()


@router.get("/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int, session: SessionDep):
    producto = session.get(Producto, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, datos: Producto, session: SessionDep):
    producto = session.get(Producto, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto.nombre = datos.nombre
    producto.precio = datos.precio
    producto.stock = datos.stock
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, session: SessionDep):
    producto = session.get(Producto, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    session.delete(producto)
    session.commit()
    return {"ok": True}