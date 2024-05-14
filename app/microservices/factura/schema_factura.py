from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class FacturaBase(BaseModel):
    id_cuenta: int
    fecha_emision: date
    fecha_vencimiento: date
    total: float

    class Config:
        orm_mode = True

class FacturaCreate(FacturaBase):
    pass

class FacturaUpdate(FacturaBase):
    pass

class FacturaInDB(FacturaBase):
    id: int

class Factura(FacturaInDB):
    pass
