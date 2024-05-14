from sqlalchemy.orm import Session
from .model_cliente import CuentaCliente
from .schema_cuenta_cliente import CuentaClienteCreate, CuentaClienteUpdate

def get_cuenta_cliente(db: Session, cuenta_id: int):
    return db.query(CuentaCliente).filter(CuentaCliente.id == cuenta_id).first()

def get_cuentas_cliente(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CuentaCliente).offset(skip).limit(limit).all()

def create_cuenta_cliente(db: Session, cuenta: CuentaClienteCreate):
    db_cuenta = CuentaCliente(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta

def update_cuenta_cliente(db: Session, cuenta_id: int, cuenta: CuentaClienteUpdate):
    db_cuenta = db.query(CuentaCliente).filter(CuentaCliente.id == cuenta_id).first()
    if db_cuenta:
        update_data = cuenta.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_cuenta, key, value)
        db.commit()
        db.refresh(db_cuenta)
    return db_cuenta

def delete_cuenta_cliente(db: Session, cuenta_id: int):
    db_cuenta = db.query(CuentaCliente).filter(CuentaCliente.id == cuenta_id).first()
    if db_cuenta:
        db.delete(db_cuenta)
        db.commit()
    return db_cuenta
