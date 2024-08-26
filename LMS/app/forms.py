from django import forms
from django.contrib.auth.models import User
from .models import Room, CustomUser




class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields =['username','email','password', 'profile']
   
class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = CustomUser
        fields = ['email','password']
  
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'Description', 'topic']  # Exclude 'host' from the fields

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super(RoomForm, self).__init__(*args, **kwargs)
        
        # Set the host field to the current user
        if user:
            self.instance.host = user

class RoomEditForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'Description','topic']