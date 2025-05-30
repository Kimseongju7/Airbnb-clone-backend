from django.core.serializers import serialize
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("pk", "name", "description", )


class RoomListSerializer(ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ("pk", "name", "country", "city", "price", "rating", "is_owner", )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True,  many=True)
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user