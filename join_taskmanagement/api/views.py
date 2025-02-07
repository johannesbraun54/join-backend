from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics
from .serializers import TaskSerializer, ContactSerializer, SubtaskSerializer, TaskGETSerializer, SummarySerializer
from join_taskmanagement.models import Task, Contact, Subtask, Summary
from .functions import check_earliest_date

############# TASK VIEWS #############


def get_task_ID(task):
    serializer = TaskGETSerializer(task)
    print(serializer.data, "data with id")
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def tasks_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskGETSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            print("task.pk", task.pk)
            get_task_ID(task)
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
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

############# CONTACT VIEWS #############


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

############# SUBTASK VIEWS #############


class SubtasksViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer


@api_view(['GET'])
def summary_view(request):
    if request.method == 'GET':
        get_earliest_date = check_earliest_date()
        summary = Summary.objects.create(tasks_in_board=len(Task.objects.all()),
                                               todo=len(Task.objects.filter(status="todo")),
                                               in_progress=len(Task.objects.filter(status="inProgress")),
                                               await_feedback=len(Task.objects.filter(status="awaitFeedback")),
                                               done=len(Task.objects.filter(status="done")),
                                               prio_urgent=len(Task.objects.filter(prio="Urgent")),
                                               earliest_due_date = get_earliest_date)
        serializer = SummarySerializer(summary)
        return Response(serializer.data)


