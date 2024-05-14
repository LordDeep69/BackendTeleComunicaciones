from sqlalchemy.orm import Session
from .model_registro_uso_servicios import RegistroUsoServicios
from .schema_registro_uso_servicios import RegistroUsoServiciosCreate, RegistroUsoServiciosUpdate

def get_registro_uso_servicios(db: Session, registro_id: int):
    return db.query(RegistroUsoServicios).filter(RegistroUsoServicios.id == registro_id).first()

def get_registros_uso_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RegistroUsoServicios).offset(skip).limit(limit).all()

def create_registro_uso_servicios(db: Session, registro: RegistroUsoServiciosCreate):
    db_registro = RegistroUsoServicios(**registro.dict())
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

def update_registro_uso_servicios(db: Session, registro_id: int, registro: RegistroUsoServiciosUpdate):
    db_registro = db.query(RegistroUsoServicios).filter(RegistroUsoServicios.id == registro_id).first()
    if db_registro:
        update_data = registro.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_registro, key, value)
        db.commit()
        db.refresh(db_registro)
    return db_registro

def delete_registro_uso_servicios(db: Session, registro_id: int):
    db_registro = db.query(RegistroUsoServicios).filter(RegistroUsoServicios.id == registro_id).first()
    if db_registro:
        db.delete(db_registro)
        db.commit()
    return db_registro
