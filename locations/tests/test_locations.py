import pytest
from locations.models import Location
from locations.utils import (GeoAdmin, GeoCountry, GeoName, get_geoadmins,
                             get_geocountries, get_geonames, populate_city,
                             populate_country, populate_location,
                             populate_region)


@pytest.fixture()
def region():
    geoadmin = GeoAdmin(
        'US.CA.085', 'Santa Clara County', 'Santa Clara County', '5393021'
    )
    region = populate_region(geoadmin)

    yield region

    region.delete()


@pytest.fixture()
def city():
    geoadmin = GeoAdmin(
        'US.CA', 'California', 'California', '5332921'
    )
    city = populate_city(geoadmin)

    yield city

    city.delete()


@pytest.fixture()
def country():
    geocountry = GeoCountry(
        'US', 'USA', '840', 'US', 'United States', 'Washington', '9629091',
        '310232863', 'NA', '.us', 'USD', 'Dollar', '1', '#####-####',
        '^\d{5}(-\d{4})?$', 'en-US,es-US,haw,fr', '6252001', 'CA,MX,CU'
    )
    country = populate_country(geocountry)

    yield country

    country.delete()


def test_load_geonames():
    geonames = get_geonames('./locations/tests/data/locations.txt')
    geoname = next(geonames)
    assert isinstance(geoname, GeoName)
    assert geoname.name


def test_load_geoadmins():
    geoadmins = get_geoadmins('./locations/tests/data/regions.txt')
    geoadmin = next(geoadmins)
    assert isinstance(geoadmin, GeoAdmin)
    assert geoadmin.name


def test_load_geocountries():
    geocountries = get_geocountries('./locations/tests/data/countries.txt')
    geocountry = next(geocountries)
    assert isinstance(geocountry, GeoCountry)
    assert geocountry.country


@pytest.mark.django_db
def test_load_location(region, city, country):
    geoname = GeoName(
        '1821261', 'Test', 'Test', '', '22.12722', '113.55028', 'H', 'BAY',
        'US', '', 'CA', '085', '', '', '0', '', '-9999', 'Asia/Macau',
        '2012-01-18'
    )
    location = populate_location(geoname)
    assert Location.objects.count() == 1
    assert location.city.id == city.id
