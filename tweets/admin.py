from django.contrib import admin
from .models import Tweet, Like

class Contains_elonmusk(admin.SimpleListFilter):
    title = "Does it contain Elon Musk?"
    parameter_name = "elonmusk"

    def lookups(self, request, model_admin):
        return (
            ("contain", "Contain"),
            ("not_contain", "Not Contain"),
        )

    def queryset(self, request, tweets):
        if self.value() == "contain":
            return tweets.filter(payload__icontains="elon musk")
        elif self.value() == "not_contain":
            return tweets.exclude(payload__icontains="elon musk")
        else:
            return tweets

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("__str__", "number_of_like", "created_at", "updated_at", )
    list_filter = ("created_at", Contains_elonmusk, )
    search_fields = ("payload", "user__username", )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("tweet", "user", "created_at", )
    list_filter = ("created_at", )
    search_fields = ("user__username", )
