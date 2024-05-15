from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.api.core.database import Base

class Dispositivo(Base):
    __tablename__ = 'Dispositivo'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('Cliente.id'))
    tipo_dispositipo = Column(String(50))
    modelo = Column(String(100))
    numero_serie = Column(String(50))
    estado = Column(String(50))
    cliente = relationship('Cliente', back_populates='dispositivos', primaryjoin='Dispositivo.cliente_id'=='Cliente.id')
