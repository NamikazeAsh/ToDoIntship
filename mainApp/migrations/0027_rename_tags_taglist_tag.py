# Generated by Django 4.0.1 on 2022-11-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_todo_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taglist',
            old_name='Tags',
            new_name='Tag',
        ),
    ]