# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, WasteDataViewSet

router = DefaultRouter()
router.register(r'inventory', FoodItemViewSet)
router.register(r'waste-data', WasteDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
