from django.contrib.auth.models import User
from django.db import models
from property.models import Property

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_property = models.OneToOneField(Property, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
