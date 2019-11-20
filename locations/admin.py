from django.contrib import admin

from .models import City, Country, Location, Region

admin.site.register(Location)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
