import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000/tasks"

def fetch_tasks():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Falha ao buscar tarefas: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Ocorreu um erro ao buscar as tarefas: {str(e)}")
        return None

def display_tasks(tasks):
    if tasks:
        cols = st.columns(3)
        for index, task in enumerate(tasks):
            created_at_formatted = format_datetime(task['created_at'])
            updated_at_formatted = format_datetime(task['updated_at'])

            with cols[index % 3]:
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; box-sizing: border-box;">
                        <h4>{task['title']}</h4>
                        <p><strong>Descrição:</strong> {task['description']}</p>
                        <p><strong>Status:</strong> {task['status']}</p>
                        <p><small><strong>Criado em:</strong> {created_at_formatted}</small></p>
                        <p><small><strong>Atualizado em:</strong> {updated_at_formatted}</small></p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.write("Nenhuma tarefa encontrada.")

def create_task(title, description):
    try:
        response = requests.post(API_URL, params={"title": title, "description": description})
        if response.status_code == 201:
            st.success("Tarefa criada com sucesso!")
            title = ""
            description = ""
        else:
            st.error(f"Falha ao criar tarefa: {response.status_code}")
    except Exception as e:
        st.error(f"Ocorreu um erro ao criar a tarefa: {str(e)}")

def format_datetime(date_str):
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime('%d %b %Y, %H:%M')
    except ValueError:
        return date_str

def main():
    st.title("Gerenciador de Tarefas")
    
    st.markdown("A documentação da API está disponível em: [TO-DO/docs](http://localhost:8000/docs)")

    st.header("Criar Nova Tarefa")
    with st.form(key="create_task_form"):
        task_title = st.text_input("Título da Tarefa")
        task_description = st.text_area("Descrição da Tarefa")
        submit_button = st.form_submit_button("Criar Tarefa")

        if submit_button:
            if task_title and task_description:
                create_task(task_title, task_description)
            else:
                st.error("Preencha o título e a descrição.")

    st.header("Lista de Tarefas")
    tasks = fetch_tasks()
    if tasks is not None:
        display_tasks(tasks)

if __name__ == "__main__":
    main()
