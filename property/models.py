from django.contrib.auth.models import User
from django.db import models

from sellers.models import Seller


# Create your models here.
class Property(models.Model):
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    size = models.DecimalField(decimal_places=2, max_digits=6)
    rooms = models.DecimalField(decimal_places=1, max_digits=4)
    bathrooms = models.DecimalField(decimal_places=1, max_digits=4)
    bedrooms = models.DecimalField(decimal_places=1, max_digits=4)
    description = models.TextField()
    additional_info = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_properties', blank=True)

    def __str__(self):
        return f"{self.address} ({self.pk})"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for {self.property.address}"



