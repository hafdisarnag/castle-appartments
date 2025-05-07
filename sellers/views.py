from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Seller

def seller_profile(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    properties = seller.property_set.all()

    return render(request, 'sellers/sellerprofile.html', {
        'seller': seller,
        'properties': properties,
    })

