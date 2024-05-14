from pydantic import BaseModel, Field

class ServicioBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    tipo: str = Field(..., max_length=50)
    tarifa: float

    class Config:
        orm_mode = True

class ServicioCreate(ServicioBase):
    pass

class ServicioUpdate(ServicioBase):
    pass

class ServicioInDB(ServicioBase):
    id: int

class Servicio(ServicioInDB):
    pass
