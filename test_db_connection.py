from app.api.core.database import SessionLocal
from sqlalchemy import text

# Crear una nueva sesión de base de datos
session = SessionLocal()

try:
    # Ejecutar una consulta simple para obtener la versión de la base de datos
    version = session.execute(text("SELECT VERSION();")).fetchone()
    print(f"La versión de la base de datos es: {version[0]}")
except Exception as e:
    print(f"Ocurrió un error al conectar con la base de datos: {e}")
finally:
    # Cerrar la sesión de base de datos
    session.close()
