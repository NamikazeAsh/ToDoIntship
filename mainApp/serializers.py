from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagList
        fields = ('Tag',)
        

class ToDoSerializer(serializers.ModelSerializer):
    
    Tag = TagSerializer(many=True)
    
    class Meta:
        model = ToDo
        fields = ('id','CreatedTimestamp','Title','Description','Date','Tag','Status')
        
        
class ToDoSerializerC(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id','Title','Description','Date','Tag','Status')
        
