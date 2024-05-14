from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .crud_cuenta_cliente import (
    get_cuenta_cliente, get_cuentas_cliente, create_cuenta_cliente,
    update_cuenta_cliente, delete_cuenta_cliente
)
from .schema_cuenta_cliente import CuentaClienteCreate, CuentaClienteUpdate, CuentaCliente
from api.core.database import get_db

router = APIRouter()

@router.get("/cuentas/", response_model=List[CuentaCliente])
def read_cuentas_cliente(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_cuentas_cliente(db, skip=skip, limit=limit)

@router.get("/cuentas/{cuenta_id}", response_model=CuentaCliente)
def read_cuenta_cliente(cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = get_cuenta_cliente(db, cuenta_id=cuenta_id)
    if cuenta is None:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return cuenta

@router.post("/cuentas/", response_model=CuentaCliente)
def create_cuenta_cliente_endpoint(cuenta: CuentaClienteCreate, db: Session = Depends(get_db)):
    return create_cuenta_cliente(db=db, cuenta=cuenta)

@router.put("/cuentas/{cuenta_id}", response_model=CuentaCliente)
def update_cuenta_cliente_endpoint(cuenta_id: int, cuenta: CuentaClienteUpdate, db: Session = Depends(get_db)):
    return update_cuenta_cliente(db, cuenta_id=cuenta_id, cuenta=cuenta)

@router.delete("/cuentas/{cuenta_id}", response_model=CuentaCliente)
def delete_cuenta_cliente_endpoint(cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = delete_cuenta_cliente(db, cuenta_id=cuenta_id)
    if cuenta is None:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return cuenta
