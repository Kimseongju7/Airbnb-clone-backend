from django.db import models
from common.models import CommonModel
# Create your models here.
class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = "entire_place", "Entire Place"
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
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms", default="",)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name= "rooms",
    )

    def __str__(self):
        return self.name

    def total_amenities(self):
        print(self)
        return self.amenities.count()
    
    def rating(self):
        tot_rating = 0
        if self.reviews.count() == 0:
            return "No Reviews"
        # query set은 게으르기에 데이터를 즉시 가지고 오지 않고, 사용할 때 가지고 옴.
        # 아래 코드에서는 가지고 오지 않음
        # self.review.all();
        # 여기서 database에서 가져옴
        for review in self.reviews.all().values("rating"):
            tot_rating += review["rating"]
        #소수점 이하 2자리까지만 표시
        return round(tot_rating / self.reviews.count(), 2)




class Amenity(CommonModel):
    """Amenity model definition"""
    name = models.CharField(max_length=150, )
    description = models.CharField(max_length=150, null=True, blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
