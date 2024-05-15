from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_notificacion import (
    get_notificacion, get_notificaciones, create_notificacion,
    update_notificacion, delete_notificacion
)
from .schema_notificacion import (
    NotificacionCreate, NotificacionUpdate, Notificacion
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

@router.get("/notificaciones/", response_model=List[Notificacion])
def read_notificaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notificaciones = get_notificaciones(db, skip=skip, limit=limit)
    return notificaciones

@router.get("/notificaciones/{notificacion_id}", response_model=Notificacion)
def read_notificacion(notificacion_id: int, db: Session = Depends(get_db)):
    db_notificacion = get_notificacion(db, notificacion_id=notificacion_id)
    if db_notificacion is None:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return db_notificacion

@router.post("/notificaciones/", response_model=Notificacion, status_code=status.HTTP_201_CREATED)
def create_new_notificacion(notificacion: NotificacionCreate, db: Session = Depends(get_db)):
    return create_notificacion(db=db, notificacion=notificacion)

@router.put("/notificaciones/{notificacion_id}", response_model=Notificacion)
def update_existing_notificacion(notificacion_id: int, notificacion: NotificacionUpdate, db: Session = Depends(get_db)):
    db_notificacion = update_notificacion(db, notificacion_id=notificacion_id, notificacion=notificacion)
    if db_notificacion is None:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return db_notificacion

@router.delete("/notificaciones/{notificacion_id}", response_model=Notificacion)
def delete_existing_notificacion(notificacion_id: int, db: Session = Depends(get_db)):
    db_notificacion = delete_notificacion(db, notificacion_id=notificacion_id)
    if db_notificacion is None:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return db_notificacion
