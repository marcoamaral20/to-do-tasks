# To-Do Tasks API

Esta é uma aplicação de gerenciamento de tarefas (to-do list) que permite criar e listar tarefas. Foi desenvolvida com FastAPI, PostgreSQL e Streamlit.

## Funcionalidades

- **Criar Tarefa**: Permite a criação de novas tarefas, com título, descrição e status (pendente ou concluída).
- **Listar Tarefas**: Exibe todas as tarefas existentes.

## Requisitos Técnicos

- FastAPI para a criação da API.
- PostgreSQL como banco de dados.
- Streamlit para uma interface de visualização das tarefas.
- Docker para facilitar a configuração e execução do ambiente.

## Tecnologias Utilizadas

- Python 3.10
- FastAPI
- PostgreSQL
- Docker & Docker Compose
- Streamlit

## Instalação

### 1. Clonando o Repositório

```bash
git clone https://github.com/marcoamaral20/to-do-tasks.git
cd to-do-tasks
```

### 2. Configuração do Docker

A aplicação utiliza o Docker para orquestrar os containers. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

Para rodar a aplicação, basta executar o seguinte comando no terminal dentro da pasta do projeto:

```bash
docker-compose up --build
```

Isso irá iniciar os containers do PostgreSQL, FastAPI e Streamlit.

### 3. Acessando a API

Após o Docker iniciar os containers, você pode acessar a documentação interativa da API (Swagger) através do seguinte URL:

- Swagger (FastAPI): http://localhost:8000/docs

### 4. Acessando a Interface Streamlit

A interface de visualização das tarefas foi construída com Streamlit e pode ser acessada em:

- Streamlit App: http://localhost:8501

## Endpoints da API

### 1. Criar Tarefa

- Método: POST
- URL: `/tasks`

Request Body:

```json
{
  "title": "Título da Tarefa",
  "description": "Descrição da Tarefa",
}
```

Exemplo de cURL:

```bash
curl -X 'POST' \
  'http://localhost:8000/tasks' \
  -H 'Content-Type: application/json' \
  -d '{ "title": "Nova Tarefa", "description": "Descrição da tarefa" }'
```

Resposta: Status 201 (Created), com a tarefa criada.

### 2. Listar Tarefas

- Método: GET
- URL: `/tasks`

Exemplo de cURL:

```bash
curl -X 'GET' 'http://localhost:8000/tasks'
```

Resposta: Lista com todas as tarefas criadas.

## Rodando Localmente

Se preferir rodar a aplicação localmente sem Docker, siga os passos abaixo.

### 1. Configuração do Ambiente

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Rodando a API

Para rodar a API FastAPI, use o comando:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

Agora você pode acessar a API no endereço: http://localhost:8000.

### 3. Rodando o Streamlit

Para rodar o Streamlit localmente, use o comando:

```bash
streamlit run streamlit/app.py
```

O Streamlit será iniciado em: http://localhost:8501.

## Configurações do Docker

A aplicação é configurada usando `docker-compose.yml`. Este arquivo define os seguintes serviços:

- PostgreSQL: Usado como banco de dados para armazenar as tarefas.
- API FastAPI: A aplicação principal que gerencia as tarefas (criação e listagem).
- Streamlit: Uma interface para visualização das tarefas.

### Docker Compose

Aqui está o conteúdo do arquivo `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres
    container_name: local_postgres
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: todo-tasks
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

  api:
    build:
      context: .
    container_name: todo_api
    working_dir: /app
    volumes:
      - ./api:/app/api
    ports:
      - "8000:8000"
    environment:
      - PYTHONPATH=/app
    command: uvicorn api.main:app --host 0.0.0.0 --port 8000
    depends_on:
      - postgres
    networks:
      - app-network

  streamlit:
    image: python:3.10-slim
    container_name: todo_streamlit
    working_dir: /app
    volumes:
      - ./streamlit:/app
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
    command: ["streamlit", "run", "app.py"]
    depends_on:
      - api
    networks:
      - app-network

volumes:
  postgres_data:
    driver: local

networks:
  app-network:
    driver: bridge
```
