# Generated by Django 4.0.1 on 2022-11-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_remove_todo_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Tag',
            field=models.ManyToManyField(to='mainApp.TagList'),
        ),
    ]
