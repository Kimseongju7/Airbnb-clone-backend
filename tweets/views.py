from django.shortcuts import render
from .models import Tweet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
from rest_framework.views import APIView
# Create your views here.

class Tweets(APIView):

    def get(self, request):
        tweets = Tweet.objects.all()
        print(tweets)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
