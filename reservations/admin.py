from django.contrib import admin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "check_in", "check_out", "experience_time", "guests", )
    list_filter = ("kind", )
