from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):  # or admin.StackedInline
    model = PropertyImage
    extra = 1  # number of extra image fields shown

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]

admin.site.register(Property, PropertyAdmin)

