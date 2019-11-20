from rest_framework import viewsets

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Locations to be viewed.
    """
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer
