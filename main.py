from fastapi import FastAPI
# from .api.v1.endpoints import cliente, cuenta_cliente, factura, pago, plan, servicio, registro_uso_servicios, empleado, notificacion, dispositivo, ticket_soporte

app = FastAPI()

# # Incluir los routers de los endpoints
# app.include_router(cliente.router)
# app.include_router(cuenta_cliente.router)
# app.include_router(factura.router)
# app.include_router(pago.router)
# app.include_router(plan.router)
# app.include_router(servicio.router)
# app.include_router(registro_uso_servicios.router)
# app.include_router(empleado.router)
# app.include_router(notificacion.router)
# app.include_router(dispositivo.router)
# app.include_router(ticket_soporte.router)

# Definir un endpoint raíz para verificar que la API está funcionando
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Ejecutar el servidor utilizando uvicorn si este archivo es el punto de entrada
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
