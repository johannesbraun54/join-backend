from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import TaskSerializer, ContactSerializer, SubtaskSerializer, TaskGETSerializer
from join_taskmanagement.models import Task, Contact, Subtask
from .functions import check_earliest_date

############# TASK VIEWS #############


def get_task_ID(task):
    serializer = TaskGETSerializer(task)
    print(serializer.data, "data with id")
    return Response(serializer.data)


class TasksViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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
        data = {
            'tasks_in_board': len(Task.objects.all()),
            'todo': len(Task.objects.filter(status="todo")),
            'in_progress': len(Task.objects.filter(status="inProgress")),
            'await_feedback': len(Task.objects.filter(status="awaitFeedback")),
            'done': len(Task.objects.filter(status="done")),
            'prio_urgent': len(Task.objects.filter(prio="Urgent")),
            'earliest_due_date': get_earliest_date
        }
        return Response(data)
