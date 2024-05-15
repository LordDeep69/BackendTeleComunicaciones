from sqlalchemy import Column, Integer, Text, DateTime, Enum, ForeignKey
from app.api.core.database import Base
from sqlalchemy.orm import relationship

class Notificacion(Base):
    __tablename__ = 'notificaciones'

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    mensaje = Column(Text, nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(Enum('enviada', 'leida'), nullable=False)
    cliente = relationship("Cliente", back_populates="notificaciones")
