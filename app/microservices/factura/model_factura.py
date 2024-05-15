from sqlalchemy import Column, Integer, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.api.core.database import Base

class Factura(Base):
    __tablename__ = 'Factura'

    id = Column(Integer, primary_key=True, index=True)
    id_cuenta = Column(Integer, ForeignKey('CuentaCliente.id'))
    fecha_emision = Column(Date)
    fecha_vencimiento = Column(Date)
    total = Column(DECIMAL(10, 2))
    cuenta_cliente = relationship('CuentaCliente', back_populates='facturas')
    pagos = relationship('Pago', back_populates='factura')
