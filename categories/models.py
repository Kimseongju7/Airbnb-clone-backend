from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):
    """ Room or Experience Category """
    class CategoriesKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50, )
    kind = models.CharField(
        max_length=15, choices=CategoriesKindChoices.choices,
    )

    def __str__(self):
        return f"{self.kind.title()} - {self.name}"

    class Meta:
        verbose_name_plural = "Categories"