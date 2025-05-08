from django.contrib.auth.models import User
from django.db import models

from property.models import Property


class Offer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='offers')
    amount = models.DecimalField("Offer Amount", max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateField("Expires On")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # ← new field

    def is_expired(self):
        from django.utils import timezone
        return timezone.now().date() > self.expires_at
