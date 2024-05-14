from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RegistroUsoServiciosBase(BaseModel):
    id_cliente: int
    id_servicio: int
    fecha_hora: datetime
    cantidad_utilizada: float

    class Config:
        orm_mode = True

class RegistroUsoServiciosCreate(RegistroUsoServiciosBase):
    pass

class RegistroUsoServiciosUpdate(RegistroUsoServiciosBase):
    pass

class RegistroUsoServiciosInDB(RegistroUsoServiciosBase):
    id: int

class RegistroUsoServicios(RegistroUsoServiciosInDB):
    pass
