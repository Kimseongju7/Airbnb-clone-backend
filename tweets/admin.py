from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("__str__", "number_of_like", "created_at", "updated_at", )
    list_filter = ("created_at", )

    def number_of_like(self, twwet):
        return twwet.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("tweet", "user", "created_at", )
    list_filter = ("created_at", )
