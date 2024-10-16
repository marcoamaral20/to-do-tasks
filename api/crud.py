from fastapi.responses import JSONResponse
from .database import database
from datetime import datetime

def serialize_task(task):
    if task:
        task_dict = dict(task)
        for key, value in task_dict.items():
            if isinstance(value, datetime):
                task_dict[key] = value.isoformat()
        return task_dict
    return task

async def create_task(title: str, description: str):
    query = """
    INSERT INTO tasks (title, description, status)
    VALUES (:title, :description, 'pendente') RETURNING id, title, description, status, created_at, updated_at;
    """
    values = {"title": title, "description": description}
    try:
        result = await database.fetch_one(query=query, values=values)
        task = serialize_task(result)
        return JSONResponse(content={"message": "Tarefa criada com sucesso!", "task": task}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": f"Erro ao criar tarefa: {str(e)}"}, status_code=500)

async def get_tasks():
    query = """
    SELECT id, title, description, status, created_at, updated_at FROM tasks;
    """
    try:
        tasks = await database.fetch_all(query=query)
        return [serialize_task(task) for task in tasks]
    except Exception as e:
        return JSONResponse(content={"error": f"Erro ao obter tarefas: {str(e)}"}, status_code=500)
