# Generated by Django 4.1.1 on 2022-11-21 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_todo_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Completed',
        ),
    ]
