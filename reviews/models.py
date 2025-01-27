from django.db import models
from common.models import CommonModel

# Create your models here.
class Review(CommonModel):
    """ Review from user to room or experience """
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, related_name="reviews",)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, null=True, blank=True, related_name="reviews",)
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE, null=True, blank=True,
        related_name="reviews",
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} : {self.room} - {self.rating}"
