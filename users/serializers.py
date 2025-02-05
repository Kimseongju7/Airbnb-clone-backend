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