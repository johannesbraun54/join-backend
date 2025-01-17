from rest_framework import serializers
from join_taskmanagement.models import Task, Contact, Subtask


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

    def create(self, validated_data):
        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'status', 'title', 'description',
                  'assigned_to', 'assigned_to_ids', 'due_date', 'prio', 'category', 'subtasks']

    assigned_to = ContactSerializer(many=True, read_only=True)
    assigned_to_ids = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(), many=True, write_only=True, source="assigned_to")
    subtasks = SubtaskSerializer(many=True, read_only=True)


class TaskGETSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    assigned_to = ContactSerializer(many=True, read_only=True)
    due_date = serializers.DateField()  # lesen
    prio = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    subtasks = SubtaskSerializer(many=True, read_only=True)

# class TaskCREATESerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     status = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)
#     assigned_to = ContactSerializer(many=True, read_only=True) # ändern
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
