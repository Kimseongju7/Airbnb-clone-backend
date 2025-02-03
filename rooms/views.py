from django.core.serializers import serialize
from rest_framework.views import APIView
from .models import Amenity
from .serializers import AmenitySerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

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