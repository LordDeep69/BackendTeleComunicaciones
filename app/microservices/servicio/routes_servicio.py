from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_servicio import get_servicio, get_servicios, create_servicio, update_servicio, delete_servicio
from .schema_servicio import ServicioCreate, ServicioUpdate, Servicio
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/servicios/", response_model=List[Servicio])
def read_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    servicios = get_servicios(db, skip=skip, limit=limit)
    return servicios

@router.get("/servicios/{servicio_id}", response_model=Servicio)
def read_servicio(servicio_id: int, db: Session = Depends(get_db)):
    db_servicio = get_servicio(db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@router.post("/servicios/", response_model=Servicio, status_code=status.HTTP_201_CREATED)
def create_new_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    return create_servicio(db=db, servicio=servicio)

@router.put("/servicios/{servicio_id}", response_model=Servicio)
def update_existing_servicio(servicio_id: int, servicio: ServicioUpdate, db: Session = Depends(get_db)):
    db_servicio = update_servicio(db, servicio_id=servicio_id, servicio=servicio)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@router.delete("/servicios/{servicio_id}", response_model=Servicio)
def delete_existing_servicio(servicio_id: int, db: Session = Depends(get_db)):
    db_servicio = delete_servicio(db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio
