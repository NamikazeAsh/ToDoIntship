# Generated by Django 4.0.1 on 2022-11-28 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_todo_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainApp.taglist'),
        ),
    ]
