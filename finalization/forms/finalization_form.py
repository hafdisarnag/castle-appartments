from django import forms

COUNTRIES = [
    ('IS', 'Iceland'),
    ('NO', 'Norway'),
    ('DK', 'Denmark'),
]

PAYMENT_METHODS = [
    ('credit_card', 'Credit Card'),
    ('bank_transfer', 'Bank Transfer'),
    ('mortgage', 'Mortgage'),
]

MORTGAGE_PROVIDERS = [
    ('arion', 'Arion banki'),
    ('landsbankinn', 'Landsbankinn'),
    ('islandsbanki', 'Íslandsbanki'),
]

class ContactForm(forms.Form):
    full_name = forms.CharField()
    national_id = forms.CharField(label="Kennitala")
    street = forms.CharField()
    city = forms.CharField()
    postal_code = forms.CharField()
    country = forms.ChoiceField(choices=COUNTRIES)

class PaymentMethodForm(forms.Form):
    payment_method = forms.ChoiceField(choices=PAYMENT_METHODS, widget=forms.RadioSelect)

class CreditCardForm(forms.Form):
    cardholder_name = forms.CharField()
    card_number = forms.CharField()
    expiry_date = forms.CharField()
    cvc = forms.CharField()

class BankTransferForm(forms.Form):
    bank_account = forms.CharField()

class MortgageForm(forms.Form):
    provider = forms.ChoiceField(choices=MORTGAGE_PROVIDERS)
