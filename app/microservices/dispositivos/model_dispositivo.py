from sqlalchemy import Column, Integer, String, ForeignKey
from api.core.database import Base
from sqlalchemy.orm import relationship

class Dispositivo(Base):
    __tablename__ = 'dispositivos'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    tipo_dispositivo = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    numero_serie = Column(String(100), nullable=False)
    estado = Column(String(50), nullable=False)
    cliente = relationship("Cliente", back_populates="dispositivos")
