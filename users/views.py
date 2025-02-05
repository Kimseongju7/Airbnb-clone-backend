from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .serializers import UserListSerializer, UserDetailSerializer, PrivateUserSerializer, PublicUserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from reviews.serializers import ReviewSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout


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

class PublicUser(APIView):

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, username):
        user = self.get_object(username)
        serializer = PublicUserSerializer(user)
        return Response(serializer.data)



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


class UserReviews(APIView):

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, username):
        user = self.get_object(username)
        serializer = ReviewSerializer(user.reviews.all(), many=True)
        return Response(serializer.data)


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Please enter your old password and new password")

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError("Old password and new password are required")
        if not user.check_password(old_password):
            raise ParseError("Wrong password")
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_200_OK)

class LogIn(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError("Username and password are required")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response("Logged in")
        else:
            raise ParseError("Wrong username or password")


class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response("Logged out")