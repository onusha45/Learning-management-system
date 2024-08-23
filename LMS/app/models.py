from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
          return self.name
     
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    room_name = models.CharField(max_length=30)
    participants =models.ManyToManyField(User, related_name='participants',blank=True)
    Description = models.TextField(max_length= 200,null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updates_date = models.DateTimeField(auto_now=True,null=True)

 
    def __str__(self) :
        return self.room_name
    class Meta:
         ordering = ['-updates_date','-created_date']



class Message(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
       room = models.ForeignKey(Room,on_delete=models.CASCADE)
       body = models.TextField()
       created_date = models.DateTimeField(auto_now_add=True,null=True)
       updates_date = models.DateTimeField(auto_now=True,null=True)
    
       def __str__(self) :
            return self.body[0:50]
       class Meta:
         ordering = ['-updates_date','-created_date']


