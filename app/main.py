from fastapi import FastAPI
from app.core.init_db import init_db
from app.api.routers.users_router import router as users_router

# Inicializar banco de dados
init_db()

app = FastAPI(
    title="Back-Eden-Map API",
    description="API para gerenciamento de usuários do Eden Map",
    version="1.0.0"
)

# Incluir rotas
app.include_router(users_router, prefix="/api/users")

@app.get("/")
def root():
    return {"message": "Welcome to Back-Eden-Map API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
