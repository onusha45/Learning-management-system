from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import room
from .forms import UserForm
from django.contrib.auth.models import User
# Create your views here.
def index (request):
    rooms = room.objects.all()
    context = {
        'rooms': rooms
    }
    return render (request,'index.html',context)
def login(request):
   
    return render (request,'login.html')
def room_list (request,pk):
    rooms = room.objects.filter(id=pk)
    context = {
        'rooms': rooms
    }
    return render(request,"room.html",context)
def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    
    context = {
        'form': form
    }
    return render(request,'register.html',context)