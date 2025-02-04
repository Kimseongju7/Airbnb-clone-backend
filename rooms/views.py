from django.core.serializers import serialize
from rest_framework.views import APIView
from .models import Amenity, Room
from categories.models import Category
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from django.db import transaction

class Rooms(APIView):
    def get(self, request):
        rooms = Room.objects.all();
        return Response(RoomListSerializer(rooms, many=True).data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data = request.data)
            if serializer.is_valid():
                # check if category is valid
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required")
                try:
                    category = Category.objects.get(pk = category_pk)
                except Category.DoesNotExist:
                    raise ParseError(f"Category_pk : {category_pk} does not exist")
                if category.kind == Category.CategoriesKindChoices.EXPERIENCES:
                    raise ParseError("Category kind should be a room")
                try:
                    with transaction.atomic():
                        new_room = serializer.save(
                            owner=request.user,
                            category = category
                        )
                        # add amenities
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            new_room.amenities.add(amenity)
                        return Response(RoomDetailSerializer(new_room).data)
                except Exception:
                    raise ParseError("Amenity not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk = pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        return Response(RoomDetailSerializer(room).data)



class Amenities(APIView):
    def get(self, request):
        amenities_all = Amenity.objects.all();
        serializer = AmenitySerializer(amenities_all, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = AmenitySerializer(data = request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk = pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        return Response(
            AmenitySerializer(self.get_object(pk)).data
        )

    def put(self, request, pk):
        serializer = AmenitySerializer(self.get_object(pk), data = request.data, partial=True)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)