from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_cliente import get_cliente, get_clientes, create_cliente, update_cliente, delete_cliente
from .schema_cliente import ClienteCreate, ClienteUpdate, Cliente
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/clientes/", response_model=List[Cliente])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = get_clientes(db, skip=skip, limit=limit)
    return clientes

@router.get("/clientes/{cliente_id}", response_model=Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@router.post("/clientes/", response_model=Cliente, status_code=status.HTTP_201_CREATED)
def create_new_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return create_cliente(db=db, cliente=cliente)

@router.put("/clientes/{cliente_id}", response_model=Cliente)
def update_existing_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    db_cliente = update_cliente(db, cliente_id=cliente_id, cliente=cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@router.delete("/clientes/{cliente_id}", response_model=Cliente)
def delete_existing_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = delete_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente
