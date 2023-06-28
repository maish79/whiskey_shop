from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    """
    A class view creating the Location form
    """
    class Meta:
        model = Location
        exclude = ['slug',]