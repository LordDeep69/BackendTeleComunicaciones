from sqlalchemy.orm import Session
from .model_factura import Factura
from .schema_factura import FacturaCreate, FacturaUpdate

def get_factura(db: Session, factura_id: int):
    return db.query(Factura).filter(Factura.id == factura_id).first()

def get_facturas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Factura).offset(skip).limit(limit).all()

def create_factura(db: Session, factura: FacturaCreate):
    db_factura = Factura(**factura.dict())
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura

def update_factura(db: Session, factura_id: int, factura: FacturaUpdate):
    db_factura = db.query(Factura).filter(Factura.id == factura_id).first()
    if db_factura:
        update_data = factura.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_factura, key, value)
        db.commit()
        db.refresh(db_factura)
    return db_factura

def delete_factura(db: Session, factura_id: int):
    db_factura = db.query(Factura).filter(Factura.id == factura_id).first()
    if db_factura:
        db.delete(db_factura)
        db.commit()
    return db_factura
