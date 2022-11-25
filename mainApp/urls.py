from django.urls import path
from .views import *

urlpatterns = [

    path('',todo,name='todo'),
    path('update/<int:pk>',todo_upd,name='todo-update'),
    path('delete/<int:pk>',todo_del,name='todo-delete'),
    path('show/<int:pk>',todo_show,name='todo-show'),
    
]