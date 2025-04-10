# api/views.py

from rest_framework import viewsets
from .models import FoodItem, WasteData
from .serializers import FoodItemSerializer, WasteDataSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class WasteDataViewSet(viewsets.ModelViewSet):
    queryset = WasteData.objects.all()
    serializer_class = WasteDataSerializer
