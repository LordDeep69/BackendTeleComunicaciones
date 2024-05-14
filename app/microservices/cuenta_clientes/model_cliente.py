from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, DECIMAL
from sqlalchemy.orm import relationship
from api.core.database import Base

class CuentaCliente(Base):
    __tablename__ = 'cuenta_cliente'

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    estado = Column(Enum('activo', 'suspendido', 'cancelado'))
    saldo = Column(DECIMAL(10, 2))
    fecha_creacion = Column(Date)
    cliente = relationship("Cliente", back_populates="cuentas")
