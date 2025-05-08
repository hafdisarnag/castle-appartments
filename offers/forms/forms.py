from django import forms
from offers.models import Offer
from django.utils import timezone
from django.core.exceptions import ValidationError

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['amount', 'expires_at']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'expires_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean_expires_at(self):
        expires_at = self.cleaned_data['expires_at']
        if expires_at < timezone.now().date():
            raise ValidationError("Expiration date cannot be in the past.")
        return expires_at