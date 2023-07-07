from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = (
        'name', 'slug', 'email', 'phone_number',
        'street_address1', 'street_address2', 'town_or_city',
        'county', 'country', 'postcode',
        'latitude', 'longitude'
    )
    list_display = ('name', 'street_address1', 'phone_number')


admin.site.register(Location, LocationAdmin)