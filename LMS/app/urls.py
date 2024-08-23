from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from .viewset import TopicViewsets,MessageViewsets,UserViewsets,RoomViewsets


# router = DefaultRouter()
# router.register('topic', TopicViewsets , basename='TopicViewsets'),
# router.register('message',MessageViewsets,basename='MessageViewsets'),
# router.register('user',UserViewsets,basename='UserViewsets'),
# router.register('room',RoomViewsets,basename='RoomViewsets')
urlpatterns = [
   
    path('', index , name='index'),
    path('room_home/',room_home,name='room_home'),
    path('user_registration/',user_registration,name='user_registration'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout',user_logout,name='user_logout'),
    path('room_list/<int:pk>/',room_list, name = 'room_list'),
    path('room_register/',room_register, name = 'room_register'),
    path('room_delete/<int:pk>/',room_delete, name = 'room_delete'),
    path('room_edit/<int:pk>/',room_edit, name = 'room_edit'),
    path('delete-message/<int:pk>/',deletemessage, name = 'delete-message'),
]