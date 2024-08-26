from django.contrib import admin
from .models import Room,Message,Topic, CustomUser
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
admin.site.register(CustomUser)