from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "price",
        "rooms",
        "toilets",
        "kind",
        "owner",
        "pet_friendly",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "category",
        "country",
        "city",
        "rooms",
        "toilets",
        "kind",
        "pet_friendly",
        "amenities",
        "created_at",
        "updated_at",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )