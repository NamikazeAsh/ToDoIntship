from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagList
        fields = ('Tag',)
        

class ToDoSerializer(serializers.ModelSerializer):
    
    Tag = TagSerializer(many=True,read_only=True)
    
    TagID = serializers.PrimaryKeyRelatedField(
        many=True,write_only = True,queryset = TagList.objects.all()
    )
    
    class Meta:
        model = ToDo
        fields = ('id','CreatedTimestamp','Title','Description','Date','Tag','TagID','Status')
    
    def create(self,validated_data):
        tag = validated_data.pop("TagID",None)
        todoz = ToDo.objects.create(**validated_data)
        if tag:
            todoz.Tag.set(tag)
        return todoz
        
        
