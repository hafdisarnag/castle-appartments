from django.http import HttpResponse
from django.shortcuts import render
from property.models import Property


def index(request):
    return render(request,"property/property.html",  {
        "properties": Property.objects.all(),
    })

def get_property_by_id(request, id):
    property = [x for x in properties if x['id'] == id][0]
    return render(request, "property/property.html", {
        "properties": property
    })

