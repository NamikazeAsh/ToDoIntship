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
        tagl = TagList.objects.values_list()
        print("Tagl ",tagl)
        
        tx = ToDo.objects.values_list('id')
        print("IDs:",tx)
        # for x in tx:
        #     # print(x[0])
        
            
        
        serializer = ToDoSerializer(ts,many=True)
        
        x = ToDo.objects.all().values()
        ll = []
        
        for jtags in tagl:
            print("jtags",jtags[1])
        
        for a in x:
            for id1 in tx:
                tagslist = []
                if a["id"]==id1[0]:
                    tt = ToDo.objects.filter(id=id1[0]).values_list('Tag')
                    print("TagQS ",tt)
                    for tn1 in tt: 
                        for tn2 in tagl:
                            if tn2[0] == tn1[0]:
                                tagslist.append(tn2[1])
                    a.update({"Tags":tagslist})
            ll.append(a)
            
        # return Response(serializer.data)
        return Response(ll)
    
    if request.method == 'POST':
        
        # ---------------------------------------------------------------------------- #
        #                           GETTING DATA FROM REQUEST                          #
        # ---------------------------------------------------------------------------- #
        # ----------------- s.data for POST and s.query_params for GET ----------------- #
        
        data=request.data 

        serializer = ToDoSerializer(data = data)
        if serializer.is_valid():
                
            # tags = data["Tag"]
            # print(tags)
            # tags = tags.split()
            
            # for tag in tags:
                
            #     if tags.count(tag) > 1:
            #         print("Repeating tag: ",tag)
            #         return Response({"Repeating tags":tag})
            #         break
                
            #     else:
            
            serializer.save()
            
            resp = {"Status":"Successfully created"}
            return Response(resp)
        
        return Response({"Error":serializer.errors})
    
@api_view(['PUT'])
def todo_upd(request,pk):
    
    taglist = TagList.objects.values_list()
    print("\nTaglist ",taglist)
    
    
    ts = ToDo.objects.get(pk=pk)
    tsv = ToDo.objects.filter(pk=pk).values('Tag')
    # serializer = ToDoSerializer(instance = ts,data = request.data)
    
    
    data = request.data
    # print("Data",data)
    print("Tags: ",tsv)
    # if serializer.is_valid():
    
    
    tags = data["Tags"]
    print("Upd tags ",tags)
    
    ts2 = ToDo(pk=pk)
    tl = []
    ts2.Title = data["Title"]
    ts2.Description = data["Description"]
    ts2.Date = data["Date"]
    ts2.Status = data["Status"]
    for tag in tags:
        for etags in taglist:
            if tag == etags[1]:
                tl.append(etags[0])
    print("TL",tl)
    print(ts2.Tag.values())
    # ts2.Tag.set(tl)
    # ts2.Tag.remove()
    # ts2.Tag.set(tl)
    ts2.Tag.clear()
    ts2.Tag.set(tl)
    ts2.save()
        
        # serializer.save()
    return Response({"Successful":"Done"})
        
    # else:
    #     return Response({"Error":serializer.errors})
    
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




