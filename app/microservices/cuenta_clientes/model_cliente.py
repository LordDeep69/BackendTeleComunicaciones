from sqlalchemy import Column, Integer, DECIMAL, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.api.core.database import Base

class CuentaCliente(Base):
    __tablename__ = 'CuentaCliente'  # Nombre de la tabla como en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('Cliente.id'))
    estado = Column(Enum('activo', 'suspendido', 'cancelado'))
    saldo = Column(DECIMAL(10, 2))
    fecha_creacion = Column(Date)
    cliente = relationship('Cliente', back_populates='cuentas', primaryjoin='CuentaCliente.id_cliente==Cliente.id')
    facturas = relationship('Factura', back_populates='cuenta_cliente', primaryjoin='CuentaCliente.id==Factura.id_cuenta')

