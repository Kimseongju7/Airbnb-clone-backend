from rest_framework import serializers
from .models import Tweet
from users.serializer import TinyUserSerializer

class TweetSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"