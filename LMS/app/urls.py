from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='index'),
    path('home/',home,name='home'),
    path('user_registration/',user_registration,name='user_registration'),
    path('login/',user_login,name='user_login'),
    path('user_logout',user_logout,name='user_logout'),
    path('room_list/<int:pk>/',room_list, name = 'room_list'),
    path('room_register/',room_register, name = 'room_register'),
]