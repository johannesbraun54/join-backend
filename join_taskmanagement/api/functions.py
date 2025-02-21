from join_taskmanagement.models import Task
import datetime

def check_earliest_date():
    if len(Task.objects.all()) > 0:
        get_earliest_date = Task.objects.all().order_by("dueDate").first().dueDate
    else:
        get_earliest_date = datetime.date.today()
    return get_earliest_date