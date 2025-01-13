from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from join_taskmanagement.models import Task


@api_view(['GET', 'POST'])
def tasks_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        tasks = Task.objects.all()
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
