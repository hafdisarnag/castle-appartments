from django.shortcuts import render, redirect
from .forms.finalization_form import *
from offers.models import Offer

def save_step(request, key, data):
    request.session[key] = data
    request.session.modified = True

def step1_contact(request, offer_id):
    request.session['offer_id'] = offer_id
    form = ContactForm(request.POST or None, initial=request.session.get('contact'))
    if form.is_valid():
        save_step(request, 'contact', form.cleaned_data)
        return redirect('finalization:step2_payment', offer_id=offer_id)
    return render(request, 'finalization/step1_contact.html', {'form': form})

def step2_payment(request, offer_id):
    form = PaymentMethodForm(request.POST or None, initial=request.session.get('payment_method'))
    if form.is_valid():
        save_step(request, 'payment_method', form.cleaned_data)
        return redirect('finalization:step3_payment_details', offer_id=offer_id)
    return render(request, 'finalization/step2_payment.html', {'form': form, 'offer_id': offer_id})


def step3_payment_details(request, offer_id):
    method = request.session.get('payment_method', {}).get('payment_method')
    form_class = {
        'credit_card': CreditCardForm,
        'bank_transfer': BankTransferForm,
        'mortgage': MortgageForm,
    }.get(method)

    if not form_class:
        return redirect('finalization:step2_payment')

    form = form_class(request.POST or None, initial=request.session.get('payment_details'))

    if form.is_valid():
        save_step(request, 'payment_details', form.cleaned_data)
        return redirect('finalization:step4_review', offer_id=offer_id)

    return render(request, 'finalization/step3_payment_details.html', {'form': form, 'method': method, 'offer_id': offer_id})

def step4_review(request, offer_id):
    context = {
        'contact': request.session.get('contact'),
        'payment_method': request.session.get('payment_method'),
        'payment_details': request.session.get('payment_details'),
        'offer_id': offer_id
    }
    if request.method == 'POST':
        offer_id = request.session.get('offer_id')

        return redirect('finalization:step5_confirmation', offer_id=offer_id)
    return render(request, 'finalization/step4_review.html', context)

def step5_confirmation(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    offer.is_finalized = True
    offer.save()

    property = offer.property
    property.is_sold = True
    property.save()

    for key in ['contact', 'payment_method', 'payment_details', 'offer_id']:
        if key in request.session:
            del request.session[key]
    return render(request, 'finalization/step5_confirmation.html')

