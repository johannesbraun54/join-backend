# Generated by Django 5.1.4 on 2025-02-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_taskmanagement', '0011_rename_assigned_to_task_assignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
