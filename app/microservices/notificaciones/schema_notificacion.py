from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class EstadoNotificacionEnum(str, Enum):
    enviada = 'enviada'
    leida = 'leida'

class NotificacionBase(BaseModel):
    id_cliente: int
    mensaje: str
    fecha_hora: datetime
    estado: EstadoNotificacionEnum

    class Config:
        orm_mode = True

class NotificacionCreate(NotificacionBase):
    pass

class NotificacionUpdate(NotificacionBase):
    pass

class NotificacionInDB(NotificacionBase):
    id: int

class Notificacion(NotificacionInDB):
    pass
