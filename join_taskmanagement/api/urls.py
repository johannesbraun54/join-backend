from django.urls import path
from .views import tasks_view, contacts_view, subtasks_view, task_detail_view

urlpatterns = [
    path('tasks/', tasks_view),
    path('tasks/<int:pk>', task_detail_view, name='task-detail'),
    path('contacts/', contacts_view),
    path('subtasks/', subtasks_view)
]
