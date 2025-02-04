from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .serializer import UserListSerializer, UserDetailSerializer
from rest_framework.views import APIView

# Create your views here.
class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        return Response(UserListSerializer(users, many=True).data)


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


class UserTweets(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweets = Tweet.objects.filter(user=self.get_object(pk))
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
