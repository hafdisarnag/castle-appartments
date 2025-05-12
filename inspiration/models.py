from django.db import models

from django.db import models

class DesignIdea(models.Model):
    image = models.ImageField(upload_to='design_ideas/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=[
        ('living', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('other', 'Other'),
    ])

    def __str__(self):
        return self.category

