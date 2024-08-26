from rest_framework import serializers
from .models import Topic, Room, Message, CustomUser
from django.contrib.auth.models import User


class TopicSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class MessageSerializers (serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
class UserSerializers (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','password']