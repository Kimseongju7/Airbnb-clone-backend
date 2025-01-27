from random import choices

from django.db import models
from common.models import CommonModel

# Create your models here.
class Experience(CommonModel):
    country = models.CharField(max_length=50, default="한국",)
    city = models.CharField(max_length=80, default="서울",)
    name = models.CharField(max_length=250, default="", )
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="experiences", default="",)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250, )
    start  = models.TimeField()
    end  = models.TimeField()
    description = models.TextField(null=True, blank=True, default="", )
    perks = models.ManyToManyField("experiences.Perk", related_name="experiences", )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name= "experiences",
    )

    def __str__(self) -> str:
        return self.name;


class Perk(CommonModel):
    """ What is included in the experience"""

    name = models.CharField(max_length=150, )
    details = models.CharField(max_length=150, default="")
    description = models.CharField(max_length=150, null=True, blank=True, )

    def __str__(self) -> str:
        return self.name;

