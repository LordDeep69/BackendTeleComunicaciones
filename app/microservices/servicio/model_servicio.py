from sqlalchemy import Column, Integer, String, DECIMAL
from api.core.database import Base

class Servicio(Base):
    __tablename__ = 'servicios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    tarifa = Column(DECIMAL(10, 2), nullable=False)
