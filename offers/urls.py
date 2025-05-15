from django.urls import path
from offers import views

urlpatterns = [
    path('make/<int:property_id>/', views.make_offer, name='make_offer'),
    path('my/', views.my_offers, name='my_offers'),
    path('remove/<int:offer_id>/', views.remove_offer, name='remove_offer'),


]