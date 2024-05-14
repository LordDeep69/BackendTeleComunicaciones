from sqlalchemy.orm import Session
from .model_dispositivo import Dispositivo
from .schema_dispositivo import DispositivoCreate, DispositivoUpdate

def get_dispositivo(db: Session, dispositivo_id: int):
    return db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()

def get_dispositivos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Dispositivo).offset(skip).limit(limit).all()

def create_dispositivo(db: Session, dispositivo: DispositivoCreate):
    db_dispositivo = Dispositivo(**dispositivo.dict())
    db.add(db_dispositivo)
    db.commit()
    db.refresh(db_dispositivo)
    return db_dispositivo

def update_dispositivo(db: Session, dispositivo_id: int, dispositivo: DispositivoUpdate):
    db_dispositivo = db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()
    if db_dispositivo:
        update_data = dispositivo.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_dispositivo, key, value)
        db.commit()
        db.refresh(db_dispositivo)
    return db_dispositivo

def delete_dispositivo(db: Session, dispositivo_id: int):
    db_dispositivo = db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()
    if db_dispositivo:
        db.delete(db_dispositivo)
        db.commit()
    return db_dispositivo
