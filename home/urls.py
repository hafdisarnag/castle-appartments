from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:9000 (root)
    path('', views.index, name='home-index'),
]