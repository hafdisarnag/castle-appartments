from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspiration_home, name='inspiration'),
]