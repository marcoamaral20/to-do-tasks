CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pendente',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Optional: Create an index to make searches faster
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks (status);

INSERT INTO tasks (title, description, status)
VALUES 
    ('Tarefa 1', 'Descrição da tarefa 1', 'pendente'),
    ('Tarefa 2', 'Descrição da tarefa 2', 'concluída'),
    ('Tarefa 3', 'Descrição da tarefa 3', 'pendente');

