from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField() # lesen
    phone = models.IntegerField() 

class Task(models.Model):
    status = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    assignedTo = models.ManyToManyField(Contact, related_name="tasks")
    dueDate = models.DateField() # lesen
    prio = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
class Subtask(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")