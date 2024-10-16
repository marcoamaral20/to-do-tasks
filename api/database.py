from databases import Database
from .config import DATABASE_URL

# Criação da instância de conexão com o banco de dados
database = Database(DATABASE_URL)

async def connect_db():
    await database.connect()
    print("Conexão com o banco de dados estabelecida!")

async def disconnect_db():
    await database.disconnect()
    print("Conexão com o banco de dados fechada!")