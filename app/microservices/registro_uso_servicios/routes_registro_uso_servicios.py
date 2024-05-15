from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_registro_uso_servicios import get_registro_uso_servicios, get_registros_uso_servicios, create_registro_uso_servicios, update_registro_uso_servicios, delete_registro_uso_servicios
from .schema_registro_uso_servicios import RegistroUsoServiciosCreate, RegistroUsoServiciosUpdate, RegistroUsoServicios
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/registros-uso-servicios/", response_model=List[RegistroUsoServicios])
def read_registros_uso_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    registros_uso_servicios = get_registros_uso_servicios(db, skip=skip, limit=limit)
    return registros_uso_servicios

@router.get("/registros-uso-servicios/{registro_id}", response_model=RegistroUsoServicios)
def read_registro_uso_servicio(registro_id: int, db: Session = Depends(get_db)):
    db_registro_uso_servicio = get_registro_uso_servicios(db, registro_id=registro_id)
    if db_registro_uso_servicio is None:
        raise HTTPException(status_code=404, detail="Registro de uso de servicio no encontrado")
    return db_registro_uso_servicio

@router.post("/registros-uso-servicios/", response_model=RegistroUsoServicios, status_code=status.HTTP_201_CREATED)
def create_new_registro_uso_servicio(registro: RegistroUsoServiciosCreate, db: Session = Depends(get_db)):
    return create_registro_uso_servicios(db=db, registro=registro)

@router.put("/registros-uso-servicios/{registro_id}", response_model=RegistroUsoServicios)
def update_existing_registro_uso_servicio(registro_id: int, registro: RegistroUsoServiciosUpdate, db: Session = Depends(get_db)):
    db_registro_uso_servicio = update_registro_uso_servicios(db, registro_id=registro_id, registro=registro)
    if db_registro_uso_servicio is None:
        raise HTTPException(status_code=404, detail="Registro de uso de servicio no encontrado")
    return db_registro_uso_servicio

@router.delete("/registros-uso-servicios/{registro_id}", response_model=RegistroUsoServicios)
def delete_existing_registro_uso_servicios(registro_id: int, db: Session = Depends(get_db)):
    db_registro_uso_servicio = delete_registro_uso_servicios(db, registro_id=registro_id)
    if db_registro_uso_servicio is None:
        raise HTTPException(status_code=404, detail="Registro de uso de servicio no encontrado")
    return db_registro_uso_servicio
