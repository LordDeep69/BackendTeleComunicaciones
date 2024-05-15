from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_dispositivo import (
    get_dispositivo, get_dispositivos, create_dispositivo,
    update_dispositivo, delete_dispositivo
)
from .schema_dispositivo import (
    DispositivoCreate, DispositivoUpdate, Dispositivo
)
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dispositivos/", response_model=List[Dispositivo])
def read_dispositivos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dispositivos = get_dispositivos(db, skip=skip, limit=limit)
    return dispositivos

@router.get("/dispositivos/{dispositivo_id}", response_model=Dispositivo)
def read_dispositivo(dispositivo_id: int, db: Session = Depends(get_db)):
    db_dispositivo = get_dispositivo(db, dispositivo_id=dispositivo_id)
    if db_dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return db_dispositivo

@router.post("/dispositivos/", response_model=Dispositivo, status_code=status.HTTP_201_CREATED)
def create_new_dispositivo(dispositivo: DispositivoCreate, db: Session = Depends(get_db)):
    return create_dispositivo(db=db, dispositivo=dispositivo)

@router.put("/dispositivos/{dispositivo_id}", response_model=Dispositivo)
def update_existing_dispositivo(dispositivo_id: int, dispositivo: DispositivoUpdate, db: Session = Depends(get_db)):
    db_dispositivo = update_dispositivo(db, dispositivo_id=dispositivo_id, dispositivo=dispositivo)
    if db_dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return db_dispositivo

@router.delete("/dispositivos/{dispositivo_id}", response_model=Dispositivo)
def delete_existing_dispositivo(dispositivo_id: int, db: Session = Depends(get_db)):
    db_dispositivo = delete_dispositivo(db, dispositivo_id=dispositivo_id)
    if db_dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return db_dispositivo
