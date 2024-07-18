from django.db import models

# Create your models here.
class room(models.Model):

    room_name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    content = models.TextField(max_length= 200,null=True)
    updates_date = models.DateTimeField(auto_now=True,null=True)
    def __str__(self) :
        return self.room_name

    