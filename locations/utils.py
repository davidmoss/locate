import csv
import logging
from collections import namedtuple

from .models import City, Country, Location, Region

log = logging.getLogger(__name__)
GeoName = namedtuple('GeoName', [
    'geonameid',
    'name',
    'asciiname',
    'alternatenames',
    'latitude',
    'longitude',
    'feature_class',
    'feature_code',
    'country_code',
    'cc2',
    'admin1_code',
    'admin2_code',
    'admin3_code',
    'admin4_code',
    'population',
    'elevation',
    'dem',
    'timezone',
    'modification_date',
])

GeoCountry = namedtuple('GeoCounty', [
    'iso',
    'iso3',
    'iso_numeric',
    'fips',
    'country',
    'capital',
    'area',
    'population',
    'continent',
    'tld',
    'currency_code',
    'currency_name',
    'phone',
    'postal_code_format',
    'postal_code_regex',
    'languages',
    'geonameid',
    'neighbours',
])

GeoAdmin = namedtuple('GeoAdmin', [
    'iso',
    'name',
    'ascii_name',
    'geonameid',
])


def get_geonames(filepath):
    """
    Load a file of tab separated locations and return a generator of Locations
    """

    with open(filepath) as tsv:
        tsv = filter(lambda row: row[0] != '#', tsv)
        for line in csv.reader(tsv, dialect="excel-tab"):
            log.debug(f'Read line: {line}')
            yield GeoName(*line)


def get_geocountries(filepath):
    """
    Load a file of tab separated locations and return a generator of Countries
    """

    with open(filepath) as tsv:
        tsv = filter(lambda row: row[0] != '#', tsv)
        for line in csv.reader(tsv, dialect="excel-tab"):
            log.debug(f'Read line: {line}')
            yield GeoCountry(*line)


def get_geoadmins(filepath):
    """
    Load a file of tab separated locations and return a generator of Admin code
    """

    with open(filepath) as tsv:
        tsv = filter(lambda row: row[0] != '#', tsv)
        for line in csv.reader(tsv, dialect="excel-tab"):
            log.debug(f'Read line: {line}')
            yield GeoAdmin(*line)


def populate_location(geoname):
    assert isinstance(geoname, GeoName), "Object needs to be a GeoName"
    location, __ = Location.objects.get_or_create(id=int(geoname.geonameid))
    location.name = geoname.name
    if geoname.country_code and geoname.country_code != '00':
        location.country = Country.objects.get(iso=geoname.country_code)
    if geoname.admin1_code and geoname.admin1_code != '00':
        location.city = City.objects.get(
            iso=f'{geoname.country_code}.{geoname.admin1_code}'
        )
    if geoname.admin2_code and geoname.admin2_code != '00':
        location.region = Region.objects.get(
            iso=(
                f'{geoname.country_code}.'
                f'{geoname.admin1_code}.'
                f'{geoname.admin2_code}'
            )
        )
    location.latitude = geoname.latitude
    location.longitude = geoname.longitude
    location.save()
    return location


def populate_country(geocountry):
    assert isinstance(geocountry, GeoCountry), "Object needs to be a GeoCountry"  # NOQA
    country, __ = Country.objects.get_or_create(id=int(geocountry.geonameid))
    country.name = geocountry.country
    country.iso = geocountry.iso
    country.save()
    return country


def populate_city(geoadmin):
    assert isinstance(geoadmin, GeoAdmin), "Object needs to be a GeoAdmin"
    city, __ = City.objects.get_or_create(id=int(geoadmin.geonameid))
    city.name = geoadmin.name
    city.iso = geoadmin.iso
    city.save()
    return city


def populate_region(geoadmin):
    assert isinstance(geoadmin, GeoAdmin), "Object needs to be a GeoAdmin"
    region, __ = Region.objects.get_or_create(id=int(geoadmin.geonameid))
    region.name = geoadmin.name
    region.iso = geoadmin.iso
    region.save()
    return region
