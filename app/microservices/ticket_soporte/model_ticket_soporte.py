from sqlalchemy import Column, Integer, Text, String, DateTime, ForeignKey
from app.api.core.database import Base
from sqlalchemy.orm import relationship

class TicketSoporte(Base):
    __tablename__ = 'TicketSoporte'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('Cliente.id'))
    descripcion_problema = Column(Text, nullable=False)
    estado_ticket = Column(String(50), nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
    fecha_resolucion = Column(DateTime)
    empleado_id = Column(Integer, ForeignKey('empleados.id'))
    cliente = relationship("Cliente", back_populates="tickets_soporte", primaryjoin='TicketSoporte.cliente_id==Cliente.id')
    empleado = relationship("Empleado", back_populates="tickets_resueltos", primaryjoin='TicketSoporte.cliente_id==Empleado.id')
