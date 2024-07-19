from django.urls import path
from .views import *
urlpatterns = [
    path('', index , name='index'),
    path('home/',home,name='home'),
    path('registration/',registration,name='registration'),
    path('login/',user_login,name='login'),
    path('User_logout',User_logout,name='User_logout'),
    path('room/<int:pk>/',room_list, name = 'room'),
]