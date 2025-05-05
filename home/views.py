from django.http import HttpResponse
from django.shortcuts import render
from property.models import Property


def index(request):
    return render(request,"home/home.html",  {
        "properties": Property.objects.all(),
    })