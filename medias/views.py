from rest_framework.views import APIView
from .models import Photo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound, PermissionDenied
# Create your views here.
class PhotoDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)
        if (photo.room and photo.room.owner != request.user) or (photo.experience and photo.experience.owner != request.user):
            raise PermissionDenied
        photo.delete()
        return Response(status=status.HTTP_200_OK)
