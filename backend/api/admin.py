from django.contrib import admin
from .models import City, Place, Food


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'best_time_to_visit']
    search_fields = ['name', 'state']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'category', 'entry_fee']
    list_filter = ['category', 'city']
    search_fields = ['name']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    list_filter = ['city']
    search_fields = ['name']
