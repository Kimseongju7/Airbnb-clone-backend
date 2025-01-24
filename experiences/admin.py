from django.contrib import admin
from .models  import Experience, Perk

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "city",
        "price",
        "start",
        "end",
    )
    list_filter = (
        "city",
        "category",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "description",
    )
    list_filter = (
        "details",
    )