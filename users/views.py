from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .serializers import UserListSerializer, UserDetailSerializer, PrivateUserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        return Response(UserListSerializer(users, many=True).data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError("Password is required")
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else :
            return Response(serializer.errors)



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
