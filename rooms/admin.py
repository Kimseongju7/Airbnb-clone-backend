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
        "rating",
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

    # model로 옮김
    # def average_reviews(self, room):
    #     tot_reviews = 0
    #     for review in room.reviews.all():
    #         tot_reviews += review.rating;
    #     return tot_reviews / room.reviews.count();


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