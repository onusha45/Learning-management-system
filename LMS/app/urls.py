from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='index'),
    path('room/<int:pk>/',room_list, name = 'room'),
]