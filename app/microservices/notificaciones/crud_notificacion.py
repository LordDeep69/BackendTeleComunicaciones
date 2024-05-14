from sqlalchemy.orm import Session
from .model_notificaciones import Notificacion
from .schema_notificacion import NotificacionCreate, NotificacionUpdate

def get_notificacion(db: Session, notificacion_id: int):
    return db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()

def get_notificaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notificacion).offset(skip).limit(limit).all()

def create_notificacion(db: Session, notificacion: NotificacionCreate):
    db_notificacion = Notificacion(**notificacion.dict())
    db.add(db_notificacion)
    db.commit()
    db.refresh(db_notificacion)
    return db_notificacion

def update_notificacion(db: Session, notificacion_id: int, notificacion: NotificacionUpdate):
    db_notificacion = db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()
    if db_notificacion:
        update_data = notificacion.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_notificacion, key, value)
        db.commit()
        db.refresh(db_notificacion)
    return db_notificacion

def delete_notificacion(db: Session, notificacion_id: int):
    db_notificacion = db.query(Notificacion).filter(Notificacion.id == notificacion_id).first()
    if db_notificacion:
        db.delete(db_notificacion)
        db.commit()
    return db_notificacion
