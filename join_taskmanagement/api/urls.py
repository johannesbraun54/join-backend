from django.urls import path
from .views import tasks_view, contacts_view, subtasks_view

urlpatterns = [
    path('tasks/', tasks_view),
    path('contacts/', contacts_view),
    path('subtasks/', subtasks_view)
]
