from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from offers.forms.forms import OfferForm
from offers.models import Offer
from property.models import Property

@login_required
def make_offer(request, property_id):
    prop = get_object_or_404(Property, pk=property_id)


    if prop.is_sold:
        return HttpResponseForbidden("This property has already been sold.")


    accepted_offer = prop.offers.filter(is_accepted=True).first()
    if accepted_offer and accepted_offer.user != request.user:
        return HttpResponseForbidden("Another offer has already been accepted for this property.")


    existing_offer = Offer.objects.filter(user=request.user, property=prop).first()

    if request.method == 'POST':
        form = OfferForm(request.POST, instance=existing_offer)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.property = prop
            offer.save()
            return redirect('my_offers')
    else:
        form = OfferForm(instance=existing_offer)

    return render(request, 'offers/offer.html', {
        'form': form,
        'property': prop,
        'existing_offer': existing_offer,
        'accepted_offer': accepted_offer
    })

@login_required
def my_offers(request):
    offers = Offer.objects.filter(user=request.user).select_related('property')
    return render(request, 'offers/offers.html', {'offers': offers})
