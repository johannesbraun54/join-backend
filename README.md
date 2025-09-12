**Join Backend** is the Django-based backend for a task management app, that helps organizations manage their tasks efficiently. Specifically for my App **Join-Taskmanagement**.
For more Informations see my respository: https://github.com/johannesbraun54/Join-Taskmanagement

## Functionality
User authentication: Management of user accounts and authentication.
Task management: Creation, editing and deletion of tasks.
API interfaces: Provision of RESTful APIs for interaction with the front end.

## Installation & Setup

### clone respository
```bash
git clone https://github.com/johannesbraun54/join-backend.git
cd join-backend
```

### create and activate venv
```bash
python3 -m venv env
# Mac and Linux:
source env/bin/activate  
# Windows: 
env\Scripts\activate
```

### install dependencies
```bash
pip install -r requirements.txt
```

### migrate database
```bash
python manage.py migrate
```

### create superuser
```bash
python manage.py createsuperuser
```

### start server
```bash
python manage.py runserver
# app is now reachable with http://127.0.0.1:8000/
```

## API endpoints

### Authentication 
* **POST** `/api/auth/login/` → User Login 
* **POST** `/api/auth/logout/` → User Logout
* **POST** `/api/auth/register/` → User Registration 

### Tasks
* **GET** `/api/tasks/` → get list of all tasks
* **POST** `/api/tasks/` → create new task
* **GET** `/api/tasks/{id}/` → retrieve details of a specific task
* **PUT** `/api/tasks/{id}/` → update tasks
* **DELETE** `/api/tasks/{id}/` → delete tasks