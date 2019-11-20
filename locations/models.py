from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=200)


class City(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)


class Region(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)


class Location(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, related_name='locations', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='locations', on_delete=models.CASCADE)
    region = models.ForeignKey(Region, related_name='locations', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
