from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from .viewset import TopicViewsets,MessageViewsets,UserViewsets,RoomViewsets


router = DefaultRouter()
router.register('topic', TopicViewsets , basename='TopicViewsets'),
router.register('message',MessageViewsets,basename='MessageViewsets'),
router.register('user',UserViewsets,basename='UserViewsets'),
router.register('room',RoomViewsets,basename='RoomViewsets')
urlpatterns = [
    path('api/',include(router.urls)),
    # path('', index , name='index'),
    # path('home/',home,name='home'),
    # path('user_registration/',user_registration,name='user_registration'),
    # path('login/',user_login,name='user_login'),
    # path('user_logout',user_logout,name='user_logout'),
    # path('room_list/<int:pk>/',room_list, name = 'room_list'),
    # path('room_register/',room_register, name = 'room_register'),
]