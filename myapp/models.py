# api/models.py

from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    expiry_date = models.DateField()
    category = models.CharField(max_length=50)  # Dairy, Meat, Bakery
    cost_per_kg = models.FloatField()

    def __str__(self):
        return self.name

class WasteData(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.category}"
