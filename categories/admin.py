from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", )
    list_filter = ("kind", )