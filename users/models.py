from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KOREAN = ("kr", "Korean")
        ENGLISH = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won" #tuple과 같은 형태
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length=150, editable=False, )
    last_name = models.CharField(max_length=150, editable=False, )
    avatar = models.ImageField(blank=True, )
    name = models.CharField(max_length=150, default="", )
    is_host = models.BooleanField(default=False, )
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, )
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, )
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices, )
    # 아무런 영향이 없음
    # rooms = ["room1", "room2", "room3", "room4", "room5", "room6", "room7", "room8", "room9", "room10", ]