from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class PlanBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    descripcion: str
    precio: Decimal

    class Config:
        orm_mode = True

class PlanCreate(PlanBase):
    pass

class PlanUpdate(PlanBase):
    pass

class PlanInDB(PlanBase):
    id: int

class Plan(PlanInDB):
    pass
