from django.urls import path, include
from .views import ContactViewSet, SubtasksViewSet,TasksViewset, summary_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'subtasks', SubtasksViewSet)
router.register(r'tasks', TasksViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', summary_view)
]
