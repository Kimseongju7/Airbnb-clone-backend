from django.contrib import admin
from .models import Review

class filter_by_word(admin.SimpleListFilter):
    title = "filter by word"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return (
            ("good", "Good"),
            ("bad", "Bad"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        )

    def queryset(self, request, reviews):
        if self.value():
            return reviews.filter(payload__icontains=self.value())
        else:
            return reviews


class good_or_bad(admin.SimpleListFilter):
    title = "good or bad"
    parameter_name = "good_or_bad"

    def lookups(self, request, model_admin):
        return (
            ("good", "Good"),
            ("bad", "Bad"),
        )

    def queryset(self, request, reviews):
        if self.value() == "good":
            return reviews.filter(rating__gte=3)
        elif self.value() == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "payload", )
    list_filter = ("rating", "room__owner__is_host", filter_by_word, good_or_bad, )

