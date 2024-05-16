from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from app.api.core.database import Base
from sqlalchemy.orm import relationship

class RegistroUsoServicios(Base):
    __tablename__ = 'RegistroUsoServicios'

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('Cliente.id'))
    id_servicio = Column(Integer, ForeignKey('Servicio.id'))
    fecha_hora = Column(DateTime, nullable=False)
    cantidad_utilizada = Column(DECIMAL(10, 2), nullable=False)
    cliente = relationship("Cliente", back_populates="registros_uso",  primaryjoin='RegistroUsoServicios.id_cliente == Cliente.id')
    servicio = relationship("Servicio", back_populates="registros_uso", primaryjoin='RegistroUsoServicios.id_servicio == Servicio.id')
    

