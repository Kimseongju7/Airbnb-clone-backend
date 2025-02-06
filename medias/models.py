from django.db import models
from common.models import CommonModel

# Create your models here.
class Photo(CommonModel):
    """photo model definition"""
    file = models.URLField()
    caption = models.CharField(max_length=140, )
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, null=True, blank=True, related_name="photos")
    experience = models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True, related_name="photos")

    def __str__(self):
        return "photo file"

class Video(CommonModel):
    """video model definition"""
    file = models.URLField()
    caption = models.CharField(max_length=140, )
    experience = models.OneToOneField("experiences.Experience", on_delete=models.CASCADE, related_name="video")

    def __str__(self):
        return "video file"