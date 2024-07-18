from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='index'),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('room/<int:pk>/',room_list, name = 'room'),
]