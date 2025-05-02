from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(f"response from {request.path}")

def get_property_by_id(request, id):
    return HttpResponse(f"response from {request.path} with id {id}")

