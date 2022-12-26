from django.contrib import admin
from .models import *

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = (
        'Title',
        'Description',
        'Date',
        'CreatedTimestamp',
        'Status',
        'get_Tags'
    )
    
    def get_Tags(self,obj):
        return "\n,".join([tags.Tag for tags in obj.Tag.all()])

admin.site.register(TagList)
admin.site.register(ToDo,ToDoAdmin)   