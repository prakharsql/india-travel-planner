from rest_framework import serializers
from .models import City, Place, Food


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'description', 'category', 'timing',
                  'entry_fee', 'latitude', 'longitude', 'image']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'description']


class CityListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for city list view."""
    class Meta:
        model = City
        fields = ['id', 'name', 'state', 'description', 'image',
                  'best_time_to_visit']


class CityDetailSerializer(serializers.ModelSerializer):
    """Full serializer for city detail view with nested places and foods."""
    places = PlaceSerializer(many=True, read_only=True)
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'state', 'description', 'best_time_to_visit',
                  'image', 'latitude', 'longitude', 'travel_tips',
                  'places', 'foods']
