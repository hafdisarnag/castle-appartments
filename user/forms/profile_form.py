from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from user.models import Profile

class ProfileForm(ModelForm):
    username = forms.CharField(max_length=150, required=True, label='Username')

    class Meta:
        model = Profile
        fields = ['favorite_property', 'profile_image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.user = user

    def save(self, commit=True):
        profile = super().save(commit=False)
        if hasattr(self, 'user'):
            self.user.username = self.cleaned_data['username']
            if commit:
                self.user.save()
        if commit:
            profile.save()
        return profile

