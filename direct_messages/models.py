from django.db import models
from common.models import CommonModel

# Create your models here.
class ChattingRoom(CommonModel):
    """ChattingRoom model definition"""
    participants = models.ManyToManyField("users.User", related_name="chatting_rooms", )
    def __str__(self):
        return "Chatting Room"

class Message(CommonModel):
    """Message model definition"""
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="messages", )
    room = models.ForeignKey("direct_messages.ChattingRoom", on_delete=models.CASCADE, related_name="messages", )
    def __str__(self):
        return f"{self.user} says: {self.message}"
