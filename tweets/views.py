from django.shortcuts import render
from .models import Tweet
from rest_framework.response import Response
from .serializers import TweetSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied, NotAuthenticated
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

class Tweets(APIView):

    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_tweet = serializer.save(user = request.user)
            return Response(TweetSerializer(new_tweet).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class TweetDetail(APIView):

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if tweet.user != request.user:
            raise PermissionDenied
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            modified_tweet = serializer.save()
            return Response(TweetSerializer(modified_tweet).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if tweet.user != request.user:
            raise PermissionDenied
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)