from django.shortcuts import render, redirect
from .forms.finalization_form import *

def save_step(request, key, data):
    request.session[key] = data
    request.session.modified = True

def step1_contact(request):
    form = ContactForm(request.POST or None, initial=request.session.get('contact'))
    if form.is_valid():
        save_step(request, 'contact', form.cleaned_data)
        return redirect('finalization:step2_payment')
    return render(request, 'finalization/step1_contact.html', {'form': form})

def step2_payment(request):
    form = PaymentMethodForm(request.POST or None, initial=request.session.get('payment_method'))
    if form.is_valid():
        save_step(request, 'payment_method', form.cleaned_data)
        return redirect('finalization:step3_payment_details')
    return render(request, 'finalization/step2_payment.html', {'form': form})

def step3_payment_details(request):
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
        return redirect('finalization:step4_review')

    return render(request, 'finalization/step3_payment_details.html', {'form': form, 'method': method})

def step4_review(request):
    context = {
        'contact': request.session.get('contact'),
        'payment_method': request.session.get('payment_method'),
        'payment_details': request.session.get('payment_details'),
    }
    if request.method == 'POST':
        return redirect('finalization:step5_confirmation')
    return render(request, 'finalization/step4_review.html', context)

def step5_confirmation(request):
    request.session.flush()
    return render(request, 'finalization/step5_confirmation.html')

