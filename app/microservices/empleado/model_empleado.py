from sqlalchemy import Column, Integer, String, Date, Enum
from api.core.database import Base

class Empleado(Base):
    __tablename__ = 'empleados'

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
