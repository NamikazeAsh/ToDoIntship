# Generated by Django 4.0.1 on 2022-11-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_remove_todo_tag_delete_taglist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tags', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
