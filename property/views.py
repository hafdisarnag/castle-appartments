from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from property.models import Property
from sellers.models import Seller
from offers.forms.forms import OfferForm
from offers.models import Offer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from .models import Property

def index(request):
    queryset = Property.objects.all()

    if request.GET:

        if 'search_filter' in request.GET:
            queryset = queryset.filter(address__icontains=request.GET['search_filter'])

        if 'postal' in request.GET:
            queryset = queryset.filter(zip__iexact=request.GET['postal'])

        if 'min_price' in request.GET:
            queryset = queryset.filter(price__gte=request.GET['min_price'])

        if 'max_price' in request.GET:
            queryset = queryset.filter(price__lte=request.GET['max_price'])

        if 'type' in request.GET and request.GET['type'].strip():
            queryset = queryset.filter(type=request.GET['type'])

        if 'rooms' in request.GET and request.GET['rooms'].strip():
            queryset = queryset.filter(rooms=request.GET['rooms'])

        if 'sort' in request.GET:
            if request.GET['sort'] == "Price: low to high":
                queryset = queryset.order_by("price")
            elif request.GET['sort'] == "Price: high to low":
                queryset = queryset.order_by("-price")
            elif request.GET['sort'] == "Newest":
                queryset = queryset.order_by("-date")
            elif request.GET['sort'] == "Street: A to Z":
                queryset = queryset.order_by("address")
            elif request.GET['sort'] == "Street: Z to A":
                queryset = queryset.order_by("-address")


        if request.user.is_authenticated:
            favorite_ids = request.user.favorite_properties.values_list('id', flat=True)
            for property in queryset:
                property.is_favorite = property.id in favorite_ids
        else:
            for property in queryset:
                property.is_favorite = False

        html = render_to_string('property/property_list_partial.html', {'properties': queryset}, request)
        return JsonResponse({'html': html})


    properties = Property.objects.all().order_by("-date")

    if request.user.is_authenticated:
        favorite_ids = request.user.favorite_properties.values_list('id', flat=True)
        for property in properties:
            property.is_favorite = property.id in favorite_ids
    else:
        for property in properties:
            property.is_favorite = False

    return render(request, "property/property.html", {
        "properties": properties,
    })

def get_property_by_id(request, id):
    property = get_object_or_404(Property, id=id)

    # Bæta við click count
    property.click_count += 1
    property.save(update_fields=['click_count'])

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


def load_more_properties(request):
    page_number = request.GET.get('page')
    properties = Property.objects.all().order_by('-id')
    paginator = Paginator(properties, 3)

    try:
        page_obj = paginator.page(page_number)
    except:
        return HttpResponse('')

    return render(request, 'property/load_more_partial.html', {'properties': page_obj})


