from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("avatar", "username", "name", )


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "avatar", "username", "name", "gender", "language", "currency", )


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"