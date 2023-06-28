from django.db import models

from django.db import models

DAYS = [
    ('Monday', 'mon'),
   ('Tuesday', 'tue'),
   ('Wednesday', 'wed'),
   ('Thursday', 'thu'),
   ('Friday', 'fri'),
   ('Saturday', 'sat'),
   ('Sunday', 'sun'),
]

class Hours(models.Model):
    day = models.CharField(
        choices=DAYS,
        max_length=9,
        default='none'
        )
    open = models.TimeField()
    close = models.TimeField()

    def __str__(self):
        return f'{self.day} from {self.open} - {self.close}'


class Location(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True)
    email = models.EmailField(max_length=256, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    opening_hours = models.ManyToManyField(Hours, related_name='opening_hours', blank=True)

    def __str__(self):
        return self.name




   
