from django.shortcuts import render
from django.http import HttpResponse
from .models import room
# Create your views here.
def index (request):
    rooms = room.objects.all()
    context = {
        'rooms': rooms
    }
    return render (request,'index.html',context)
def room_list (request,pk):
    rooms = room.objects.filter(id=pk)
    context = {
        'rooms': rooms
    }
    return render(request,"room.html",context)