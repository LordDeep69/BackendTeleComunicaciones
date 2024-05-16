from sqlalchemy import Column, Integer, Text, DateTime, Enum, ForeignKey
from app.api.core.database import Base
from sqlalchemy.orm import relationship

class Notificacion(Base):
    __tablename__ = 'Notificacion'

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('Cliente.id'))
    mensaje = Column(Text, nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(Enum('enviada', 'leida'), nullable=False)
    cliente = relationship("Cliente", back_populates="notificaciones", primaryjoin='Notificacion.id_cliente == Cliente.id')

