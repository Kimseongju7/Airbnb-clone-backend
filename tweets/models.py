from django.db import models
from common.models import CommonModel

# Create your models here.
class Tweet(CommonModel):
    """Tweet model definition"""
    payload = models.CharField(max_length=180, )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, default="", related_name="tweets", )
    def __str__(self):
        return f"{self.user} says: {self.payload}"

class Like(CommonModel):
    """Like model definition"""
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE, related_name="likes", )
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="likes", )
    def __str__(self):
        return f"{self.user} likes"