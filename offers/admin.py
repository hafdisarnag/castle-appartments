from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'amount', 'is_accepted', 'expires_at')
    list_filter = ('is_accepted',)
    search_fields = ('user__username', 'property__address')

