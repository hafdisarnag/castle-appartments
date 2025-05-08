from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = Profile
        fields = ['profile_image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.user = user

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        self.user.username = self.cleaned_data['username']
        if commit:
            self.user.save()
            profile.user = self.user
            profile.save()
        return profile
