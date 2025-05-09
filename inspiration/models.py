from django.db import models

from django.db import models

class DesignIdea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='design_ideas/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=[
        ('living', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('other', 'Other'),
    ])

    def __str__(self):
        return self.title

