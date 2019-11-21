from django import forms
from django.contrib import admin

from .models import City, Country, Location, Region
from .utils import get_geocountries, populate_country


class LocationForm(forms.ModelForm):
    file = forms.FileField(label='Import from file', required=False)


class LocationAdmin(admin.ModelAdmin):
    form = LocationForm


class CountriesForm(forms.ModelForm):
    file = forms.FileField(label='Import from file', required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        file = self.cleaned_data.get('file')
        if file:
            for geocountry in get_geocountries(file):
                populate_country(geocountry)
        if commit:
            instance.save()
        return instance


class CountriesAdmin(admin.ModelAdmin):
    form = CountriesForm


admin.site.register(Location, LocationAdmin)
admin.site.register(Country, CountriesAdmin)
admin.site.register(Region)
admin.site.register(City)
