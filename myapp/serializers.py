# api/serializers.py

from rest_framework import serializers
from .models import FoodItem, WasteData

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class WasteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteData
        fields = '__all__'
