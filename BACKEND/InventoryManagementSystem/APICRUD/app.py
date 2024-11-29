from fastapi import FastAPI
from routes.routes import router  # Importa las rutas

app = FastAPI()

# Registra las rutas en la aplicación
app.include_router(router)
