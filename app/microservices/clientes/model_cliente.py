from sqlalchemy import Column, Integer, String, Date
from api.core.database import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    direccion = Column(String(255))
    telefono = Column(String(20))
    correo = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    foto = Column(String(255))
    fecha_registro = Column(Date)

    # Aquí puedes agregar métodos de instancia o de clase si es necesario
