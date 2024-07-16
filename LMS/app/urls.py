from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='index'),
    path('room/',room_list, name = 'room'),
]