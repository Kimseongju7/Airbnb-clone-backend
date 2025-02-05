from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from .models import User
from reviews.serializers import ReviewSerializer
from rest_framework import serializers

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("avatar", "username", "name", )


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "name", "gender", "language", "currency", )


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )


class PublicUserSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True)
    number_of_rooms = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("avatar", "username", "name", "gender", "language", "currency", "reviews", "number_of_rooms", )

    def get_number_of_rooms(self, user):
        return user.rooms.count();
#