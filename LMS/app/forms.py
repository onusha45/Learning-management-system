from django import forms
from django.contrib.auth.models import User
from .models import room




class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =['username','email','password']
   
class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = User
        fields = ['email','password']
  
class RoomForm(forms.ModelForm):
    class Meta:
        model = room
        fields = ['room_name', 'Description','host','topic']

class RoomEditForm(forms.ModelForm):
    class Meta:
        model = room
        fields = ['room_name', 'Description','topic']