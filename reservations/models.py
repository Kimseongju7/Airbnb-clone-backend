from django.db import models

from common.models import CommonModel


# Create your models here.
class Reservation(CommonModel):
    """reservatoin models definition"""
    class ReservaionKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"
    kind = models.CharField(max_length=20, choices=ReservaionKindChoices.choices, )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reservations", default="", )
    room = models.ForeignKey("rooms.Room", on_delete=models.SET_NULL, null=True, blank=True, related_name="reservations", )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name="reservations",
    )
    check_in = models.DateField(null=True, blank=True, )
    check_out = models.DateField(null=True, blank=True, )
    experience_time = models.DateTimeField(null=True, blank=True, )
    guests = models.PositiveIntegerField()

    def __str__(self):
        if self.kind == "room":
            return f"{self.kind.title()}-{self.room} for: {self.user}"
        else:
            return f"{self.kind.title()}-{self.experience} for: {self.user}"