from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:9000 (root)
    path('property/', views.index, name='property-index'),
    path('property/<int:id>', views.get_property_by_id, name='property-by-id'),
    path('seller/<int:id>', views.get_seller_by_id, name='seller-by-id'),
    path('property/load-more/', views.load_more_properties, name='load-more-properties'),
]