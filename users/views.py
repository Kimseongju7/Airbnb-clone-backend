from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

# Create your views here.
@api_view(['GET'])
def user_tweets(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    tweets = Tweet.objects.filter(user=pk)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
