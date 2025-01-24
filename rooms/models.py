from django.db import models
from common.models import CommonModel
# Create your models here.
class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = "endtire_place", "Entire Place"
        PRIVATE_ROOM = "private_room", "Private Room"
        SHARED_ROOM = "shared_room", "Shared Room"

    """Room model definition"""
    name = models.CharField(max_length=180, default="", )
    country = models.CharField(max_length=50, default="한국",)
    city = models.CharField(max_length=80, default="서울",)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    descriptions = models.TextField(default="", )
    address = models.CharField(max_length=250, )
    pet_friendly = models.BooleanField(default=True, )
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices, )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    def __str__(self):
        return self.name




class Amenity(CommonModel):
    """Amenity model definition"""
    name = models.CharField(max_length=150, )
    description = models.CharField(max_length=150, null=True, blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
