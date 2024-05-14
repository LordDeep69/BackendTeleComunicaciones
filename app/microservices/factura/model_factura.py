from sqlalchemy import Column, Integer, DECIMAL, Date, ForeignKey
from api.core.database import Base
from sqlalchemy.orm import relationship

class Factura(Base):
    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True, index=True)
    id_cuenta = Column(Integer, ForeignKey('cuenta_clientes.id'))
    fecha_emision = Column(Date, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)
    cuenta_cliente = relationship("CuentaCliente", back_populates="facturas")
