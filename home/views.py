from django.shortcuts import render
from property.models import Property
from sellers.models import Seller
from openhouses.views import get_upcoming_open_houses

def index(request):
    open_houses = get_upcoming_open_houses()
    all_properties = Property.objects.all()
    featured_properties = Property.objects.order_by('-date')[:3]
    popular_properties = Property.objects.order_by('-click_count')[:10]

    favorite_ids = set()
    if request.user.is_authenticated:
        favorite_ids = set(request.user.favorite_properties.values_list('id', flat=True))

    def mark_favorites(properties):
        for prop in properties:
            prop.is_favorite = prop.id in favorite_ids
        return properties

    open_houses = mark_favorites(open_houses)
    all_properties = mark_favorites(all_properties)
    featured_properties = mark_favorites(featured_properties)
    popular_properties = mark_favorites(popular_properties)

    return render(request, "home/home.html", {
        "properties": all_properties,
        "featured_properties": featured_properties,
        "popular_properties": popular_properties,
        "open_houses": open_houses,
        "agencies": Seller.objects.filter(seller_type="agency"),
    })
