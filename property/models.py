from django.db import models

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
    date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address} ({self.pk})"



