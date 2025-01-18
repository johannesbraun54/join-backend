from django.db import models
import datetime
# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField() # lesen
    phone = models.IntegerField() 

class Task(models.Model):
    status = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    assigned_to = models.ManyToManyField(Contact, related_name="tasks", blank=True)
    due_date = models.DateField(datetime.datetime.today, null=True) 
    prio = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
class Subtask(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")