from django.shortcuts import render, get_object_or_404
from django.views import generic, View

# Create your views here.
from .models import Location

model = Location
queryset = Location.objects.all()
template_name = 'locations/locations.html'


class LocationList(generic.ListView):

    
  def get(self, request, slug, *args, **kwargs):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, slug=slug)

        context = {
            'location': location,
        }
        return render(request, 'locations/location_detail.html', context)