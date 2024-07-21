from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class room(models.Model):
    
    room_name = models.CharField(max_length=30)
    Description = models.TextField(max_length= 200,null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updates_date = models.DateTimeField(auto_now=True,null=True)
 
    def __str__(self) :
        return self.room_name

class Message(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
       room = models.ForeignKey(room,on_delete=models.CASCADE)
       body = models.TextField()
       created_date = models.DateTimeField(auto_now_add=True,null=True)
       updates_date = models.DateTimeField(auto_now=True,null=True)
    
       def __str__(self) :
            return f"Message ID :{self.id}"