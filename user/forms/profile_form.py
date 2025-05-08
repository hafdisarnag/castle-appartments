from django.forms import ModelForm
from user.models import Profile
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['favorite_property', 'profile_image']
