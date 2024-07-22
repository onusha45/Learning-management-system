from django.contrib import admin
from .models import room,Message,Topic
# Register your models here.
admin.site.register(room)
admin.site.register(Message)
admin.site.register(Topic)