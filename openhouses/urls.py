from django.urls import path
from . import views

urlpatterns = [
    path('load-more-openhouses/', views.load_more_openhouses, name='load-more-openhouses'),
]
