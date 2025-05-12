from django.shortcuts import render
from property.models import Property
from openhouses.views import get_upcoming_open_houses

def index(request):
    return render(request, "home/home.html", {
        "properties": Property.objects.all(),
        "featured_properties": Property.objects.order_by('-date')[:3],
        "open_houses": get_upcoming_open_houses(),
})
