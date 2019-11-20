from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.LocationViewSet, basename='Estimate')

app_name = "locations"
urlpatterns = [
    path('', include(router.urls)),
]
