from django.db import models

# Create your models here.
class room(models.Model):
    room_name = models.CharField(max_length=30)
    created_date = models.DateTimeField()
    content = models.TextField(max_length= 200,null=True)

    def __str__(self) :
        return self.room_name
