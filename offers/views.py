from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from offers.forms.forms import OfferForm
from offers.models import Offer
from property.models import Property
from django.contrib import messages

@login_required
def make_offer(request, property_id):
    prop = get_object_or_404(Property, pk=property_id)

    if prop.is_sold:
        return HttpResponseForbidden("This property has already been sold.")

    accepted_offer = prop.offers.filter(status='accepted').first()
    if accepted_offer and accepted_offer.user != request.user:
        return HttpResponseForbidden("Another offer has already been accepted for this property.")

    existing_offer = Offer.objects.filter(user=request.user, property=prop).first()

    if request.method == 'POST':
        form = OfferForm(request.POST, instance=existing_offer)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.property = prop
            offer.status = 'pending'
            offer.save()
            messages.success(request, "Your offer has been submitted successfully and is now pending.")
            return redirect('property-by-id', id=property_id)
    else:
        form = OfferForm(instance=existing_offer)

    return render(request, 'property/property_detail.html', {
        'form': form,
        'property': prop,
        'existing_offer': existing_offer,
        'accepted_offer': accepted_offer
    })

@login_required
def my_offers(request):
    offers = Offer.objects.filter(user=request.user).select_related('property')
    return render(request, 'offers/offers.html', {'offers': offers})

@login_required
def remove_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id, user=request.user)
    if offer.status == 'rejected' or offer.status == 'pending':
        offer.delete()
        messages.success(request, "Offer removed.")
    else:
        messages.error(request, "You can only remove pending or rejected offers.")
    return redirect('my_offers')