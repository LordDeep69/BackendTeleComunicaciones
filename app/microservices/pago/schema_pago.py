from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PagoBase(BaseModel):
    id_factura: int
    monto: float
    fecha_pago: date
    metodo_pago: str

    class Config:
        orm_mode = True

class PagoCreate(PagoBase):
    pass

class PagoUpdate(PagoBase):
    pass

class PagoInDB(PagoBase):
    id: int

class Pago(PagoInDB):
    pass
