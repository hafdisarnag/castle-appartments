from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from offers.forms.forms import OfferForm
from offers.models import Offer
from property.models import Property

@login_required
def make_offer(request, property_id):
    prop = get_object_or_404(Property, pk=property_id)

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.property = prop
            offer.save()
            return redirect('my_offers')  # Or redirect back to property detail
    else:
        form = OfferForm()

    return render(request, 'offers/offer.html', {'form': form, 'property': prop})

@login_required
def my_offers(request):
    offers = Offer.objects.filter(user=request.user).select_related('property')
    return render(request, 'offers/offers.html', {'offers': offers})