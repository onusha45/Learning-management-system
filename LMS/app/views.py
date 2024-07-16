from django.shortcuts import render
from django.http import HttpResponse
from .models import room
# Create your views here.
def index (request):
    return render (request,'index.html')
def room_list (request):
    rooms = room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request,"room.html",context)