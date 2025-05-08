from django.forms import ModelForm
from user.models import Profile
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'id']
        widgets = {
            'favorite_property': forms.Select(attrs={'class': 'form-control'}),
            'profile_image': forms.TextInput(attrs={'class': 'form-control'}),
        }
