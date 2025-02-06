from rest_framework import serializers
from join_taskmanagement.models import Task, Contact, Subtask, Summary


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'



class SubtaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtask
        exclude = []

    task = serializers.PrimaryKeyRelatedField(read_only=True)
    task_id = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), write_only=True, source="task")


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'status', 'title', 'description',
                  'assignedTo', 'assigned_to_ids', 'dueDate', 'prio', 'category', 'subtasks']
        
    assignedTo = ContactSerializer(many=True, read_only=True)
    assigned_to_ids = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(), many=True, write_only=True, source="assignedTo")
    subtasks = SubtaskSerializer(many=True, read_only=True)


class TaskGETSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    assignedTo = ContactSerializer(many=True, read_only=True)
    dueDate = serializers.DateField()  # lesen
    prio = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    subtasks = SubtaskSerializer(many=True, read_only=True)
    
class SummarySerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Summary
            exclude = []
        

# class TaskCREATESerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     status = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)
#     assignedTo = ContactSerializer(many=True, read_only=True) # ändern
#     due_date = serializers.DateField() # lesen
#     prio = serializers.CharField(max_length=255)
#     category = serializers.CharField(max_length=255)
#     subtasks = SubtaskSerializer(many=True)

#     def create(self, validated_data):
#         task = Task.objects.create(**validated_data)
#         # subtask = Subtask.objects.all()
#         print(validated_data)
#         # subtasks = validated_data.pop('subtasks')
#         # Subtask.objects.create(subtasks)
#         return task
