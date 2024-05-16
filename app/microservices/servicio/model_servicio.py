from sqlalchemy import Column, Integer, String, DECIMAL
from app.api.core.database import Base
from sqlalchemy.orm import relationship

class Servicio(Base):
    __tablename__ = 'Servicio'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    tarifa = Column(DECIMAL(10, 2), nullable=False)
    registros_uso = relationship('RegistroUsoServicios', back_populates='servicio', primaryjoin='Servicio.id==RegistroUsoServicios.id_servicio')
