from pydantic import BaseModel, Field

class DispositivoBase(BaseModel):
    cliente_id: int
    tipo_dispositivo: str = Field(..., max_length=100)
    modelo: str = Field(..., max_length=100)
    numero_serie: str = Field(..., max_length=100)
    estado: str = Field(..., max_length=50)

    class Config:
        orm_mode = True

class DispositivoCreate(DispositivoBase):
    pass

class DispositivoUpdate(DispositivoBase):
    pass

class DispositivoInDB(DispositivoBase):
    id: int

class Dispositivo(DispositivoInDB):
    pass
