# Locations
App to manage and access the locations around the world

## Design
After analysing the data source from geonames you have a selection of XX.zip files which contain a tab deliminated list of locations with reference to their country, city and region. The countries, cities and regions are contained within separate files that need importing appropriately. The admin import could either accept a very cumbersum zip upload of each file which would take an administrator ages. Alternatively a sync button could allow inform the system to fetch the data directly from source as a background task in celery.

Modelling the various entities we can build a relational database of all the locations, countries, cities and regions.

The API can then be exposed using Django Rest Framework (DRF) to allow listing, search and retrieval.

### Models
Location - Country, City, Region, latitude and longitude
Country - code, name
City - code, name
Region - code, name

## Setup
Initialise your virtual environment and install dependencies:
```
$ pipenv install
$ pipenv shell
```

## Usage
To run the application on http://localhost:8000:
```
$ ./manage.py runserver
```

## Tests
To run the tests:
```
$ pytest
```

## TODO
- Admin page to import in data from geonames
- Admin page to view the locations
- API to access the locations
