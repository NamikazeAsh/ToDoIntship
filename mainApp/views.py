from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *

#CRUD Operations with REST

@api_view(['GET','POST','PUT'])
def todo(request):
    
    if request.method == 'GET':
            
        ts = ToDo.objects.all()
        serializer = ToDoSerializer(ts,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data=request.data
        serializer = ToDoSerializer(data = data)
        if serializer.is_valid():
                
            tags = data["Tag"]
            tags = tags.split()
            
            for tag in tags:
                
                if tags.count(tag) > 1:
                    print("Repeating tag: ",tag)
                    return Response({"Repeating tags":tag})
                    break
                
                else:
                    serializer.save()
            
            resp = {"Status":"Successfully created"}
            return Response(resp)
        return Response({"Error":serializer.errors})
    
@api_view(['PUT'])
def todo_upd(request,pk):
    
    ts = ToDo.objects.get(pk=pk)
    serializer = ToDoSerializer(instance = ts,data = request.data)
    
    if serializer.is_valid():
        
        serializer.save()
        return Response({"Successful":"Done"})
        
    else:
        return Response({"Error":serializer.errors})
    
@api_view(['DELETE'])
def todo_del(request, pk):
    ts = get_object_or_404(ToDo,pk=pk)
    ts.delete()
    return Response({"Status":"Deleted!"})

@api_view(['GET'])
def todo_show(request,pk):
    ts = ToDo.objects.get(pk=pk)
    serializer = ToDoSerializer(instance=ts)
    return Response(serializer.data)




