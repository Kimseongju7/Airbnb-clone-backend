from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "price",
        "kind",
        "owner",
        "pet_friendly",
        "total_amenities",
        "created_at",
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

    def total_amenities(self, room):
        print(room.amenities.all())
        return room.amenities.count()


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