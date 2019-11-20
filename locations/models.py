from django.db import models


class Country(models.Model):
    iso = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=200)


class City(models.Model):
    iso = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)


class Region(models.Model):
    iso = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=200)


class Location(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, related_name='locations', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, related_name='locations', on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, related_name='locations', on_delete=models.CASCADE, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
