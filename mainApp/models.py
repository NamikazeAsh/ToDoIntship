from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class ToDo(models.Model):
    CreatedTimestamp = models.DateTimeField(default=timezone.now)
    Title = models.CharField(max_length=100,blank=False)
    Description = models.CharField(max_length=100,blank=True)
    Date = models.DateField(blank=False)
    Tag = models.CharField(max_length=20,default="-")
    StatusChoices = (
    ("OPEN","OPEN"),
    ("WORKING","WORKING"),
    ("DONE","DONE"),
    ("OVERDUE","OVERDUE")
    )
    Status = models.CharField(max_length=20,choices=StatusChoices,default="OPEN")
    
    
    def __str__(self):
        return self.Title
