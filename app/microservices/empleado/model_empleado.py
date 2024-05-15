from sqlalchemy import Column, Integer, String, Date, Enum
from app.api.core.database import Base
from sqlalchemy.orm import relationship

class Empleado(Base):
    __tablename__ = 'Empleado'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(250), nullable=False)
    contrasena = Column(String(250), nullable=False)
    foto = Column(String(250))
    puesto = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=False)
    estado_laboral = Column(Enum('activo', 'inactivo'), nullable=False)
    fecha_registro = Column(Date, nullable=False)
    tickets_resueltos = relationship('TicketSoporte', back_populates='empleado', primaryjoin='Empleado.id==TicketSoporte.empleado_id')
