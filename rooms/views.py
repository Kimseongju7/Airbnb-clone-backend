from django.core.serializers import serialize
from rest_framework.views import APIView
from .models import Amenity, Room
from categories.models import Category
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied
)
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from django.db import transaction
from reviews.serializers import ReviewSerializer
from django.conf import settings
from medias.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Rooms(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        rooms = Room.objects.all();
        return Response(
            RoomListSerializer(
                rooms,
                many=True,
                context={
                    'request':request,
                }
            ).data
        )

    def post(self, request):
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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk = pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        return Response(
            RoomDetailSerializer(
                room,
                context={
                    'request':request,
                }
            ).data
        )

    def put(self, request, pk):
        room = self.get_object(pk)
        category = room.category
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != room.owner:
            raise PermissionDenied
        serializer = RoomDetailSerializer(room, data = request.data, partial=True)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if category_pk:
                try:
                    category = Category.objects.get(pk = category_pk)
                except Category.DoesNotExist:
                    raise ParseError(f"Category_pk : {category_pk} does not exist")
                if category.kind == Category.CategoriesKindChoices.EXPERIENCES:
                    raise ParseError("Category kind should be a room")
            try:
                with transaction.atomic():
                    serializer.save(category = category)
                    amenities = request.data.get("amenities")
                    if amenities:
                        room.amenities.clear()
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                    return Response(RoomDetailSerializer(room).data)
            except Exception:
                raise ParseError("Amenity not found")
        else:
            return Response(serializer.errors)


    def delete(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != room.owner:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)




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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class RoomReviews(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk = pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = page * page_size
        room = self.get_object(pk)
        serializer = ReviewSerializer(room.reviews.all()[start:end], many=True)
        return Response(serializer.data)


class RoomAmenities(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk = pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = page * page_size
        room = self.get_object(pk)
        serializer = AmenitySerializer(room.amenities.all()[start:end], many=True)
        return Response(serializer.data)


class RoomPhotos(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk = pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        if not request.user.is_authenticated:
            raise NotAuthenticated
        room = self.get_object(pk)
        if request.user != room.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(room=room)
            return Response(PhotoSerializer(photo).data)
        else:
            return Response(serializer.errors)
