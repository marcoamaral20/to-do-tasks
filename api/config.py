DB_HOST = "postgres"
DB_PORT = "5432"
DB_NAME = "todo-tasks"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"