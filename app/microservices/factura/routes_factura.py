from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .crud_factura import get_factura, get_facturas, create_factura, update_factura, delete_factura
from .schema_factura import FacturaCreate, FacturaUpdate, Factura
from app.api.core.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/facturas/", response_model=List[Factura])
def read_facturas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    facturas = get_facturas(db, skip=skip, limit=limit)
    return facturas

@router.get("/facturas/{factura_id}", response_model=Factura)
def read_factura(factura_id: int, db: Session = Depends(get_db)):
    db_factura = get_factura(db, factura_id=factura_id)
    if db_factura is None:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return db_factura

@router.post("/facturas/", response_model=Factura, status_code=status.HTTP_201_CREATED)
def create_new_factura(factura: FacturaCreate, db: Session = Depends(get_db)):
    return create_factura(db=db, factura=factura)

@router.put("/facturas/{factura_id}", response_model=Factura)
def update_existing_factura(factura_id: int, factura: FacturaUpdate, db: Session = Depends(get_db)):
    db_factura = update_factura(db, factura_id=factura_id, factura=factura)
    if db_factura is None:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return db_factura

@router.delete("/facturas/{factura_id}", response_model=Factura)
def delete_existing_factura(factura_id: int, db: Session = Depends(get_db)):
    db_factura = delete_factura(db, factura_id=factura_id)
    if db_factura is None:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return db_factura
