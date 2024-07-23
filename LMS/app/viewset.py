from rest_framework import viewsets
from .models import Topic,room,Message
from django.contrib.auth.models import User
from .serializers import TopicSerilizers,UserSerializers,MessageSerializers,RoomSerializers

class TopicViewsets(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerilizers

class UserViewsets(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializers

class MessageViewsets(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers


class RoomViewsets(viewsets.ModelViewSet):
    queryset = room.objects.all()
    serializer_class= RoomSerializers