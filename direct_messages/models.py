from django.db import models
from common.models import CommonModel

# Create your models here.
class ChattingRoom(CommonModel):
    """ChattingRoom model definition"""
    participants = models.ManyToManyField("users.User", )
    def __str__(self):
        return "Chatting Room"

class Message(CommonModel):
    """Message model definition"""
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, )
    room = models.ForeignKey("direct_messages.ChattingRoom", on_delete=models.CASCADE, )
    def __str__(self):
        return f"{self.user} says: {self.message}"
