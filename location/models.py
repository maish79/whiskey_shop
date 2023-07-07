from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    email = models.EmailField(max_length=256, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    
    
    def __str__(self):
        return self.name