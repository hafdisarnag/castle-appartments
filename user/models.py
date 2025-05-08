from django.contrib.auth.models import User
from django.db import models
from property.models import Property

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username