from sqlalchemy.orm import Session
from .model_empleado import Empleado
from .schema_empleado import EmpleadoCreate, EmpleadoUpdate

def get_empleado(db: Session, empleado_id: int):
    return db.query(Empleado).filter(Empleado.id == empleado_id).first()

def get_empleados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Empleado).offset(skip).limit(limit).all()

def create_empleado(db: Session, empleado: EmpleadoCreate):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def update_empleado(db: Session, empleado_id: int, empleado: EmpleadoUpdate):
    db_empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if db_empleado:
        update_data = empleado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_empleado, key, value)
        db.commit()
        db.refresh(db_empleado)
    return db_empleado

def delete_empleado(db: Session, empleado_id: int):
    db_empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if db_empleado:
        db.delete(db_empleado)
        db.commit()
    return db_empleado
