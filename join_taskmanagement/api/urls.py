from django.urls import path, include
from .views import tasks_view, task_detail_view,  ContactViewSet, SubtasksViewSet, subtasks_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'subtasks', SubtasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', tasks_view),
    # path('subtasks/', subtasks_view),
    path('tasks/<int:pk>', task_detail_view, name='task-detail'),
]
