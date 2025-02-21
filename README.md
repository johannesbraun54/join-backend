Join Backend is the Django-based backend for a task management app,
that helps organizations manage their tasks efficiently.

Functions
User authentication: Management of user accounts and authentication.
Task management: Creation, editing and deletion of tasks.
API interfaces: Provision of RESTful APIs for interaction with the front end.

clonse respository
git clone https://github.com/johannesbraun54/join-backend.git

python3 -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate

install dependenies
pip install -r requirements.txt

migrate database
python manage.py migrate

create superuser
python manage.py createsuperuser

start server
python manage.py runserver

app is now reachable with http://127.0.0.1:8000/

API endpoints
Authentication:

POST /api/auth/login/: User login
POST /api/auth/logout/: User logout
POST /api/auth/register/: User registration
Tasks:

GET /api/tasks/: Retrieve list of all tasks
POST /api/tasks/: Create new task
GET /api/tasks/{id}/: Retrieve details of a specific task
PUT /api/tasks/{id}/: Update existing task
DELETE /api/tasks/{id}/: Delete task
