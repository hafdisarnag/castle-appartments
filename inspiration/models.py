from django.db import models

# Create your models here.
from django.db import models

class DesignIdea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    category = models.CharField(max_length=100, choices=[
        ('living', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('other', 'Other'),
    ])

    def __str__(self):
        return self.title
