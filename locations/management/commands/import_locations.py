from django.core.management.base import BaseCommand
from locations.utils import get_geonames, populate_location


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('filepath', nargs='+', type=str)

    def handle(self, *args, **options):
        filepath = options['filepath']
        for geoname in get_geonames(filepath):
            populate_location(geoname)
        self.stdout.write(
            self.style.SUCCESS('Successfully imported locations')
        )
