from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(modeladmin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display = (
        "name", "country", "price", "kind", "owner",
        "pet_friendly", "rating", "created_at",
    )

    list_filter = (
        "category", "country", "kind", "pet_friendly",
    )

    search_fields = ("name", "owner__username",)

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