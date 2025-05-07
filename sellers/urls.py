from django.urls import path
from . import views

urlpatterns = [
    path('<int:seller_id>/', views.seller_profile, name='seller_profile'),
]
