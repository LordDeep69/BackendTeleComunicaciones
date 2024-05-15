from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_pago import get_pago, get_pagos, create_pago, update_pago, delete_pago
from .schema_pago import PagoCreate, PagoUpdate, Pago
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pagos/", response_model=List[Pago])
def read_pagos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pagos = get_pagos(db, skip=skip, limit=limit)
    return pagos

@router.get("/pagos/{pago_id}", response_model=Pago)
def read_pago(pago_id: int, db: Session = Depends(get_db)):
    db_pago = get_pago(db, pago_id=pago_id)
    if db_pago is None:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return db_pago

@router.post("/pagos/", response_model=Pago, status_code=status.HTTP_201_CREATED)
def create_new_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    return create_pago(db=db, pago=pago)

@router.put("/pagos/{pago_id}", response_model=Pago)
def update_existing_pago(pago_id: int, pago: PagoUpdate, db: Session = Depends(get_db)):
    db_pago = update_pago(db, pago_id=pago_id, pago=pago)
    if db_pago is None:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return db_pago

@router.delete("/pagos/{pago_id}", response_model=Pago)
def delete_existing_pago(pago_id: int, db: Session = Depends(get_db)):
    db_pago = delete_pago(db, pago_id=pago_id)
    if db_pago is None:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return db_pago
