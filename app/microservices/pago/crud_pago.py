from sqlalchemy.orm import Session
from .model_pago import Pago
from .schema_pago import PagoCreate, PagoUpdate

def get_pago(db: Session, pago_id: int):
    return db.query(Pago).filter(Pago.id == pago_id).first()

def get_pagos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pago).offset(skip).limit(limit).all()

def create_pago(db: Session, pago: PagoCreate):
    db_pago = Pago(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

def update_pago(db: Session, pago_id: int, pago: PagoUpdate):
    db_pago = db.query(Pago).filter(Pago.id == pago_id).first()
    if db_pago:
        update_data = pago.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_pago, key, value)
        db.commit()
        db.refresh(db_pago)
    return db_pago

def delete_pago(db: Session, pago_id: int):
    db_pago = db.query(Pago).filter(Pago.id == pago_id).first()
    if db_pago:
        db.delete(db_pago)
        db.commit()
    return db_pago
