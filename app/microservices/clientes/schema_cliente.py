from pydantic import BaseModel, EmailStr, Field
from datetime import date

class ClienteBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo: EmailStr
    contrasena: str = Field(..., min_length=8)

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
