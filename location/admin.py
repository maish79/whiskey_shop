from django.contrib import admin
from .models import Location


class HoursAdminInline(admin.TabularInline):
    model = Location.opening_hours.through
    list_display = ('day', 'open', 'close')


class LocationAdmin(admin.ModelAdmin):
    inlines = (HoursAdminInline,)
    prepopulated_fields = ({'slug': ('name',)})
    fields = ('name', 'slug', 'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city',
              'county', 'country', 'postcode',
              'latitude', 'longitude',)
    list_display = ('name', 'street_address1', 'phone_number')


admin.site.register(Location, LocationAdmin)