# Generated by Django 5.1.4 on 2025-01-18 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_taskmanagement', '0003_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name=datetime.datetime.today),
        ),
    ]
