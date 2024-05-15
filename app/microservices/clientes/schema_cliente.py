from pydantic import BaseModel, EmailStr, Field
from datetime import date

class ClienteBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    direccion: str = Field(..., max_length=100)
    telefono: str = Field(..., max_length=100)
    correo: EmailStr
    contrasena: str = Field(..., min_length=8)
    foto: str = Field(..., max_length=100)
    fecha_registro: str = Field(..., max_length=100)

    class Config:
        orm_mode = True

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class ClienteInDB(ClienteBase):
    id: int
    fecha_registro: date

class Cliente(ClienteInDB):
    pass
