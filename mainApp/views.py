from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

#CRUD Operations with REST

class ListTodo(generics.ListAPIView):   #Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):   #Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class ShowTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateTodo(generics.CreateAPIView):   #Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializerC
    
class DeleteTodo(generics.DestroyAPIView):   #Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer