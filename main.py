from fastapi import FastAPI
from app.microservices.clientes.routes_cliente import router as cliente_router
from app.microservices.cuenta_clientes.routes_cuenta_clientes import router as cuenta_cliente_router
from app.microservices.factura.routes_factura import router as factura_router
from app.microservices.pago.routes_pago import router as pago_router
from app.microservices.dispositivos.routes_dispositivo import router as dispositivo_router
from app.microservices.empleado.routes_empleado import router as empleado_router
from app.microservices.ticket_soporte.routes_ticket_soporte import router as ticket_router
from app.microservices.servicio.routes_servicio import router as servicio_router
from app.microservices.notificaciones.routes_notificacion import router as notificaciones_router
from app.microservices.registro_uso_servicios.routes_registro_uso_servicios import router as registr_router
from app.microservices.plan.routes_plan import router as plan_router





# Importar los demás routers aquí

app = FastAPI()

# Registrar los routers
app.include_router(cliente_router)
app.include_router(cuenta_cliente_router)
app.include_router(factura_router)
app.include_router(pago_router)
app.include_router(dispositivo_router)
app.include_router(empleado_router)
app.include_router(ticket_router)
app.include_router(servicio_router)
app.include_router(notificaciones_router)
app.include_router(registr_router)
app.include_router(plan_router)




# Registrar los demás routers aquí

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Telecomunicaciones"}

# Ejecutar el servidor utilizando uvicorn si este archivo es el punto de entrada
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
