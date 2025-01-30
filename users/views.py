from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import UserTweetsSerializer
from tweets.models import Tweet

# Create your views here.
@api_view(['GET'])
def user_tweets(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    tweets = Tweet.objects.filter(user=pk)
    serializer = UserTweetsSerializer(tweets, many=True)
    return Response(serializer.data)
