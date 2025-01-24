from django.db import models
from common.models import CommonModel

# Create your models here.
class Photo(CommonModel):
    """photo model definition"""
    file = models.ImageField()
    caption = models.CharField(max_length=140, )
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, null=True, blank=True)
    experience = models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "photo file"

class Video(CommonModel):
    """video model definition"""
    file = models.FileField()
    caption = models.CharField(max_length=140, )
    experience = models.OneToOneField("experiences.Experience", on_delete=models.CASCADE)

    def __str__(self):
        return "video file"