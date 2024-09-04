import streamlit as st
import sqlite3
import pandas as pd

# Database connection
conn = sqlite3.connect('task_management.db')
c = conn.cursor()

# Database setup
def create_db():
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT, task_description TEXT, due_date TEXT, status TEXT, assigned_to TEXT)")

create_db()

# TASK FUNCTIONS

def add_task(task_name, task_description, due_date, assigned_to):
    c.execute("INSERT INTO tasks (task_name, task_description, due_date, status, assigned_to) VALUES (?, ?, ?, ?, ?)",
              (task_name, task_description, due_date, "Pending", assigned_to))
    conn.commit()

def view_tasks():
    task_query = c.execute("SELECT * FROM tasks")
    tasks = task_query.fetchall()
    return tasks

def update_task_status(task_id, status):
    c.execute("UPDATE tasks SET status=? WHERE task_id=?", (status, task_id))
    conn.commit()

def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE task_id=?", (task_id,))
    conn.commit()

def task_functions():
    st.title("Task Management System")
    functions = st.sidebar.selectbox("Select Task Functions", [
        "Add Task", "View Tasks", "Update Task Status", "Delete Task"])

    if functions == "Add Task":
        st.header("Add New Task")
        with st.form(key='new_task_details'):
            task_name = st.text_input("Task Name")
            task_description = st.text_area("Task Description")
            due_date = st.date_input("Due Date")
            assigned_to = st.text_input("Assigned To")
            submitted = st.form_submit_button("Add Task")
        if submitted and task_name:
            add_task(task_name, task_description, due_date, assigned_to)
            st.success("Task Added Successfully!")

    elif functions == "View Tasks":
        st.header("View All Tasks")
        tasks = view_tasks()
        if tasks:
            df = pd.DataFrame(tasks, columns=[
                "Task ID", "Task Name", "Task Description", "Due Date", "Status", "Assigned To"])
            st.dataframe(df)
        else:
            st.error("No tasks available.")

    elif functions == "Update Task Status":
        st.header("Update Task Status")
        task_id = st.number_input("Enter Task ID:", min_value=1)
        status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
        if st.button("Update Status"):
            update_task_status(task_id, status)
            st.success("Task Status Updated Successfully!")

    elif functions == "Delete Task":
        st.header("Delete Task")
        task_id = st.number_input("Enter Task ID to delete:", min_value=1)
        if st.button("Delete Task"):
            delete_task(task_id)
            st.success(f"Task with ID {task_id} has been deleted.")

task_functions()
conn.close()
