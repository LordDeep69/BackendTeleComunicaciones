from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class CuentaClienteBase(BaseModel):
    id_cliente: int
    estado: str = Field(..., example="activo")
    saldo: float = Field(..., example=0.0)
    fecha_creacion: str = Field(...,  max_length=100)

    class Config:
        orm_mode = True

class CuentaClienteCreate(CuentaClienteBase):
    pass

class CuentaClienteUpdate(CuentaClienteBase):
    fecha_creacion: Optional[date] = None

class CuentaClienteInDB(CuentaClienteBase):
    id: int
    fecha_creacion: date

class CuentaCliente(CuentaClienteInDB):
    pass
