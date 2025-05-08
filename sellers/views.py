from django.shortcuts import render, get_object_or_404
from .models import Seller

def seller_profile(request, seller_id):
    # Nær í seller út frá ID eða skilar 404 ef ekki til
    seller = get_object_or_404(Seller, id=seller_id)

    # Sækir allar eignir sem tengjast þessum seller og raðar þeim eftir dagsetningu
    properties = seller.properties.order_by('-date')

    return render(request, 'sellers/sellerprofile.html', {
        'seller': seller,
        'properties': properties,
    })
