from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.api.core.database import Base

class Cliente(Base):
    __tablename__ = 'Cliente'  # Nombre de la tabla como en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    direccion = Column(String(255))
    telefono = Column(String(20))
    correo = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    foto = Column(String(255))
    fecha_registro = Column(Date)
    cuentas = relationship('CuentaCliente', back_populates='cliente', primaryjoin='Cliente.id==CuentaCliente.id_cliente')
    dispositivos = relationship('Dispositivo', back_populates='cliente', primaryjoin='Cliente.id==Dispositivo.cliente_id')
    tickets_soporte = relationship('TicketSoporte', back_populates='cliente', primaryjoin='Cliente.id==TicketSoporte.cliente_id')
