from django.db import models

class Seller(models.Model):
    SELLER_TYPES = [
        ('individual', 'Individual'),
        ('agency', 'Real Estate Agency'),
    ]

    name = models.CharField(max_length=255)
    seller_type = models.CharField(
        max_length=20,
        choices=SELLER_TYPES,
        default='individual'
    )
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to='sellers/logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='sellers/covers/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


