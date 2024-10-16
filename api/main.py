from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.crud import get_tasks, create_task
from api.database import connect_db, disconnect_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Evento de inicialização
    await connect_db()
    yield
    # Evento de encerramento
    await disconnect_db()

app = FastAPI(lifespan=lifespan)

# Rotas da aplicação
@app.get("/")
async def read_root():
    return {"message": "API running"}

# Outras rotas para tarefas
@app.post("/tasks")
async def create_new_task(title: str, description: str):
    return await create_task(title, description)

@app.get("/tasks")
async def fetch_tasks():
    return await get_tasks()