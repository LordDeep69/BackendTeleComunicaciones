from sqlalchemy import Column, Integer, String, Text, DECIMAL
from api.core.database import Base

class Plan(Base):
    __tablename__ = 'planes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
