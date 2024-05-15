from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_empleado import (
    get_empleado, get_empleados, create_empleado,
    update_empleado, delete_empleado
)
from .schema_empleado import EmpleadoCreate, EmpleadoUpdate, Empleado
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/empleados/", response_model=List[Empleado])
def read_empleados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    empleados = get_empleados(db, skip=skip, limit=limit)
    return empleados

@router.get("/empleados/{empleado_id}", response_model=Empleado)
def read_empleado(empleado_id: int, db: Session = Depends(get_db)):
    db_empleado = get_empleado(db, empleado_id=empleado_id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_empleado

@router.post("/empleados/", response_model=Empleado, status_code=status.HTTP_201_CREATED)
def create_new_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    return create_empleado(db=db, empleado=empleado)

@router.put("/empleados/{empleado_id}", response_model=Empleado)
def update_existing_empleado(empleado_id: int, empleado: EmpleadoUpdate, db: Session = Depends(get_db)):
    db_empleado = update_empleado(db, empleado_id=empleado_id, empleado=empleado)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_empleado

@router.delete("/empleados/{empleado_id}", response_model=Empleado)
def delete_existing_empleado(empleado_id: int, db: Session = Depends(get_db)):
    db_empleado = delete_empleado(db, empleado_id=empleado_id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_empleado
