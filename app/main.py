from fastapi import FastAPI
from sqlmodel import select
from app.db import create_all_tables, SessionDep
from app.routes import usuarios, productos
from app.models import Usuario, Producto

app = FastAPI(
    title="API FastAPI - AWS EC2 + RDS",
    description="API RESTful con operaciones CRUD desplegada en AWS",
    version="1.0.0",
    lifespan=create_all_tables,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/check-db")
def check_db(session: SessionDep):
    result = session.exec(select(Usuario)).first()
    return {"db_status": "ok"}


app.include_router(usuarios.router)
app.include_router(productos.router)