from sqlalchemy import Column, Integer, DECIMAL,String, Date, ForeignKey
from api.core.database import Base
from sqlalchemy.orm import relationship

class Pago(Base):
    __tablename__ = 'pagos'

    id = Column(Integer, primary_key=True, index=True)
    id_factura = Column(Integer, ForeignKey('facturas.id'))
    monto = Column(DECIMAL(10, 2), nullable=False)
    fecha_pago = Column(Date, nullable=False)
    metodo_pago = Column(String(50), nullable=False)
    factura = relationship("Factura", back_populates="pagos")
