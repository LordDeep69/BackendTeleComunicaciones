from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class EmpleadoBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo: str = Field(..., max_length=250)
    contrasena: str = Field(..., max_length=250)
    foto: Optional[str] = Field(None, max_length=250)
    puesto: str = Field(..., max_length=100)
    departamento: str = Field(..., max_length=100)
    estado_laboral: str = Field(..., max_length=50)
    fecha_registro: date

    class Config:
        orm_mode = True

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(EmpleadoBase):
    pass

class EmpleadoInDB(EmpleadoBase):
    id: int

class Empleado(EmpleadoInDB):
    pass
