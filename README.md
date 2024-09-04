# Task Management System

This project is a **Task Management System** built with **Streamlit** and **SQLite**. The system allows users to create, view, update, and delete tasks, and it keeps track of task status and assignment.

## Features
- **Add Task**: Users can add a new task with a description, due date, and assign it to a user.
- **View Tasks**: Displays a list of all tasks with details such as task name, description, due date, status, and assigned person.
- **Update Task Status**: Change the status of a task (e.g., from 'Pending' to 'In Progress' or 'Completed').
- **Delete Task**: Remove a task from the system.

## Technologies Used
- **Streamlit**: A Python framework for building web applications.
- **SQLite**: A lightweight, file-based database for data storage.

## Live Demo

You can try the application live on Streamlit:

[Task Management System - Live Demo](https://task-managementgit-eul8dzfhabhslmzgybpyuw.streamlit.app/)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository/task-management.git
```
###2. Install Required Libraries
```bash
pip install streamlit pandas sqlite3
```
###3. Run the Application
```python
python -m streamlit run main.py
```

## How to Use

### Add Task
1. Navigate to the **Add Task** section from the sidebar.
2. Enter task details such as task name, description, due date, and the person to whom it is assigned.
3. Click on the **"Add Task"** button to save the task.

### View Tasks
1. Navigate to the **View Tasks** section from the sidebar.
2. All tasks will be displayed in a table format, showing task details and status.

### Update Task Status
1. Navigate to the **Update Task Status** section.
2. Enter the **Task ID** and select the new status from the dropdown (`Pending`, `In Progress`, `Completed`).
3. Click on **"Update Status"** to save the changes.

### Delete Task
1. Navigate to the **Delete Task** section.
2. Enter the **Task ID** of the task you want to delete.
3. Click on **"Delete Task"** to remove the task from the system.


### Project Structure
```bash
task-management/
│
├── task_management.py     # Main application script
├── railway.db             # SQLite database for tasks
└── README.md              # Project documentation
```
### Future Enhancements
- User authentication to restrict access to task creation and modification.
- Task priority levels (e.g., Low, Medium, High).
- Email notifications for assigned tasks.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.
