from django.http import HttpResponse
from django.shortcuts import render
from property.models import Property

def index(request):
    return render(request,"property/property.html",  {
        "properties": Property.objects.all(),
    })

def get_property_by_id(request, id):
    property = Property.objects.get(id=id)
    return render(request, "property/property_detail.html", {
        "property": property
    })
