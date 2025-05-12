from django.contrib.auth.models import User
from django.db import models
from sellers.models import Seller
import requests

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
    is_sold = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.address} ({self.pk})"

    def has_accepted_offer(self):
        return self.offers.filter(status='accepted').exists()

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            full_address = f"{self.address}, {self.city}, {self.zip}"
            self.latitude, self.longitude = self.geocode_address(full_address)
        super().save(*args, **kwargs)

    def geocode_address(self, address):
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
        headers = {'User-Agent': 'CastleApartmentsBot/1.0'}  # Required by Nominatim
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
        return None, None

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for {self.property.address}"


