from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models  import Q
from .models import Room ,Topic,Message
from .forms import UserRegisterForm,UserLogin,RoomForm,RoomEditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index (request):
   
    return render (request,'index.html')


@login_required
def room_home (request):
    q =request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
         Q(topic__name__icontains=q) |
         Q(room_name__icontains=q) |
         Q(Description__icontains=q)
         )
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {
        'room_count': room_count,
        'rooms': rooms,
        'topics': topics,
        'room_messages':room_messages,
    }
   
    return render (request,'room_home.html',context)


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
                    return redirect('room_home')  # Redirect to the home page or any other page
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
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created_date')
    participants =room.participants.all()
    if request.method =='POST':
        messsage = Message.objects.create(
            user =request.user,
            room=room,
            body= request.POST.get('body')

        )
        room.participants.add(request.user)
        return redirect('room_list',pk=room.id)
   
    context = {
        'participants':participants,
        'room': room,
        'room_messages':room_messages,
    }
    
    return render(request,"room_list.html",context)

@login_required
def room_register(request):
     if request.method == 'POST':
        form = RoomForm(request.POST, user=request.user)  # Pass the current user
        if form.is_valid():
            form.save()
            return redirect('room_home')
     else:
        form = RoomForm(user=request.user)  # Pass the current user for GET requests
    
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
            return redirect('user_login')
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



@login_required
def room_delete(request,pk):
      rooms = Room.objects.get(id=pk)
      if request.user != rooms.host:
       return HttpResponse('You are not allowed here !!')
      if request.method == 'POST':
       rooms.delete()
       return redirect('room_home')
      return render (request, 'room_registration',{'obj':rooms})


@login_required
def room_edit(request,pk):
    rooms = Room.objects.get(id=pk)
    form = RoomForm(instance=rooms)
    if request.user != rooms.host:
        return HttpResponse('You are not allowed here !!')
    if request.method == "POST":
        form =RoomEditForm(request.POST,instance=rooms)
        if form.is_valid():
            form.save()
            return redirect('room_home')
    form = RoomEditForm(instance=rooms)
    context = {
        'room_form': form
    }
    return render(request ,'room_edit.html',context)

@login_required
def deletemessage(request,pk):
      message = Message.objects.get(id=pk)
      if request.user != message.user:
       return HttpResponse('You are not allowed here !!')
      if request.method == 'POST':
       message.delete()
       return redirect('room_home')
      return render (request, 'delete_message.html',{'obj':message})
