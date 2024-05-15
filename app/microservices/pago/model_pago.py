from sqlalchemy import Column, Integer, DECIMAL, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.api.core.database import Base

class Pago(Base):
    __tablename__ = 'Pago'

    id = Column(Integer, primary_key=True, index=True)
    id_factura = Column(Integer, ForeignKey('Factura.id'))
    monto = Column(DECIMAL(10, 2))
    fecha_pago = Column(Date)
    metodo_pago = Column(String(50))
    factura = relationship('Factura', back_populates='pagos', primaryjoin='Pago.id_factura==Factura.id')
