from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ContactSerializer, SubtaskSerializer, TaskGETSerializer
from join_taskmanagement.models import Task, Contact, Subtask


@api_view(['GET', 'POST'])
def tasks_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskGETSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET','PUT', 'DELETE'])
def task_detail_view(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    
    
    if request.method == 'DELETE':
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response({"message": "Task successfully deleted."}, status=204)


@api_view(['GET', 'POST'])
def contacts_view(request):
    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET', 'POST'])
def subtasks_view(request):
    if request.method == 'GET':
        subtasks = Subtask.objects.all()
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SubtaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
