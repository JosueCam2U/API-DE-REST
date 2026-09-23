from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine
from app.config import settings

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, echo=True, connect_args=connect_args)


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]