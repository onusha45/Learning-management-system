from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import room
from .forms import UserRegisterForm,UserLogin,RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index (request):
   
    return render (request,'index.html')
@login_required
def home (request):
    rooms = room.objects.all()
    context = {
        'rooms': rooms
    }
    return render (request,'home.html',context)


def user_login(request):
     if request.method == 'POST':
        loginform = UserLogin(request.POST)
        if loginform.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            # Authenticate using the email field
            try:
                username = User.objects.get(email=email).username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to the home page or any other page
                else:
                    loginform.add_error(None, "Invalid email or password")
            except User.DoesNotExist:
                loginform.add_error(None, "Invalid email or password")
     else:
        loginform = UserLogin()
     context = {
        'loginform': loginform
    }
     return render(request, 'user_login.html',context)

@login_required
def room_list (request,pk):
    rooms = room.objects.filter(id=pk)
    context = {
        'rooms': rooms
    }
    return render(request,"room_list.html",context)

@login_required
def room_register(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'room_list' with the name of your URL pattern for listing rooms
    else:
        form = RoomForm()
    
    context = {
        'room_form': form
    }
    return render(request, "roomregistration.html", context)


def user_registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request,'user_register.html',context)
@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')