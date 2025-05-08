from django.urls import path
from . import views

app_name = 'finalization'

urlpatterns = [
    path('step1/<int:offer_id>/', views.step1_contact, name='step1_contact'),
    path('step2/<int:offer_id>/', views.step2_payment, name='step2_payment'),
    path('step3/<int:offer_id>/', views.step3_payment_details, name='step3_payment_details'),
    path('step4/<int:offer_id>/', views.step4_review, name='step4_review'),
    path('step5/<int:offer_id>/', views.step5_confirmation, name='step5_confirmation'),
]