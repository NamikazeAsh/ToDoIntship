# Generated by Django 4.1.1 on 2022-11-21 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_todo_createdtimestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='CreatedTimestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 21, 27, 57, 202778)),
        ),
    ]
