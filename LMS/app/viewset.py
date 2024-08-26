from rest_framework import viewsets
from .models import Topic,Room,Message, CustomUser
from django.contrib.auth.models import User
from .serializers import TopicSerilizers,UserSerializers,MessageSerializers,RoomSerializers

class TopicViewsets(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerilizers

class UserViewsets(viewsets.ModelViewSet):
    queryset =  CustomUser.objects.all()
    serializer_class = UserSerializers

class MessageViewsets(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers


class RoomViewsets(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class= RoomSerializers