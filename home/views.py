from django.shortcuts import render
from property.models import Property
from sellers.models import Seller
from openhouses.views import get_upcoming_open_houses

def index(request):
    open_houses = get_upcoming_open_houses()

    # Bætum við is_favorite flaggi fyrir hvern property
    if request.user.is_authenticated:
        user_favorites = request.user.favorite_properties.all()
        favorite_ids = set(user_favorites.values_list('id', flat=True))
        for prop in open_houses:
            prop.is_favorite = prop.id in favorite_ids
    else:
        for prop in open_houses:
            prop.is_favorite = False

    return render(request, "home/home.html", {
        "properties": Property.objects.all(),
        "featured_properties": Property.objects.order_by('-date')[:3],
        "open_houses": open_houses,
        "agencies": Seller.objects.filter(seller_type="agency"),
    })

