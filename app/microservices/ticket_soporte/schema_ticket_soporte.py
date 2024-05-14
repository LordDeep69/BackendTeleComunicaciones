from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TicketSoporteBase(BaseModel):
    cliente_id: int
    descripcion_problema: str
    estado_ticket: str
    fecha_creacion: datetime
    fecha_resolucion: Optional[datetime]
    empleado_id: Optional[int]

    class Config:
        orm_mode = True

class TicketSoporteCreate(TicketSoporteBase):
    pass

class TicketSoporteUpdate(TicketSoporteBase):
    pass

class TicketSoporteInDB(TicketSoporteBase):
    id: int

class TicketSoporte(TicketSoporteInDB):
    pass
