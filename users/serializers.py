from rest_framework import serializers
from .models import User
from tweets.models import Tweet

class UserTweetsSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    payload = serializers.CharField(required=True, max_length=180)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['payload', 'created_at']