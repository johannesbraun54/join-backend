# Generated by Django 5.1.4 on 2025-02-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_taskmanagement', '0014_summary_earliest_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='earliest_due_date',
            field=models.DateField(),
        ),
    ]
