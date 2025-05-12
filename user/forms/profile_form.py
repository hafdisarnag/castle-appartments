from django import forms
from django.contrib.auth.models import User
from user.models import Profile

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Profile
        fields = ['profile_image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            if hasattr(user, 'profile'):
                self.fields['phone_number'].initial = user.profile.phone_number
            self.user = user

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        self.user.username = self.cleaned_data['username']
        self.user.email = self.cleaned_data['email']
        if commit:
            self.user.save()
            profile.user = self.user
            profile.phone_number = self.cleaned_data['phone_number']
            profile.save()
        return profile