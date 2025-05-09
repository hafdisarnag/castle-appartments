from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from property.models import Property
from sellers.models import Seller
from offers.forms.forms import OfferForm
from offers.models import Offer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

def index(request):
    if 'search_filter' in request.GET:
        return JsonResponse({
            'data': [{
                'type': x.type,
                'address': x.address,
                'zip': x.zip,
                'city': x.city,
                'size': x.size,
                'rooms': x.rooms,
                'bathrooms': x.bathrooms,
                'bedrooms': x.bedrooms,
                'price': x.price,
                'id': x.id,
                'image': x.images.first().image_url if x.images.exists() else None,

            } for x in Property.objects.filter(address__icontains=request.GET['search_filter']) .order_by('id')],
        })
    return render(request,"property/property.html",  {
        "properties": Property.objects.all(),
    })


def get_property_by_id(request, id):
    property = get_object_or_404(Property, id=id)

    existing_offer = None
    accepted_offer = None
    form = None

    if request.user.is_authenticated:
        existing_offer = Offer.objects.filter(user=request.user, property=property).first()
        accepted_offer = property.offers.filter(is_accepted=True).first()
        form = OfferForm(instance=existing_offer)


    return render(request, "property/property_detail.html", {
        "property": property,
        "form": form,
        "existing_offer": existing_offer,
        "accepted_offer": accepted_offer,
    })


def get_seller_by_id(request, id):
    seller = Seller.objects.get(id=id)
    return render(request, "sellers/sellerprofile.html", {
        "seller": seller,
    })
