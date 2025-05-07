from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from property.models import Property
from sellers.models import Seller


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
    property = Property.objects.get(id=id)
    return render(request, "property/property_detail.html", {
        "property": property
    })

def get_seller_by_id(request, id):
    seller = Seller.objects.get(id=id)
    return render(request, "sellers/sellerprofile.html", {
        "seller": seller,
    })

