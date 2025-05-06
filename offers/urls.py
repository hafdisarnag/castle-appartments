from django.urls import path
from . import views
urlpatterns = [
    # http://localhost:9000 (root)
    path('offers/', views.index, name='offers-index'),

]