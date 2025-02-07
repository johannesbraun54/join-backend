from django.db import models
import datetime
# Create your models here.

class Contact(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.EmailField() # lesen
    phone = models.CharField(max_length=25) 

class Task(models.Model):
    status = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    assignedTo = models.ManyToManyField(Contact, related_name="tasks", blank=True)
    dueDate = models.DateField() 
    prio = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    
class Subtask(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")

class Summary(models.Model):
    tasks_in_board = models.IntegerField()
    todo = models.IntegerField()
    in_progress = models.IntegerField()
    await_feedback = models.IntegerField()
    done = models.IntegerField()
    prio_urgent = models.IntegerField()
    earliest_due_date = models.DateField()