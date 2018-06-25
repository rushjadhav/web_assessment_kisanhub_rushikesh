"""
Management command to populate data in database
"""

import logging

from django.db import transaction
from django.core.management.base import BaseCommand, CommandError

from weather_data.models import Region, MonthlyWeather
from weather_data_scraper.WeatherAPI import WeatherAPI, RequestFailedException
from weather_data_scraper.WeatherDataProcessor import WeatherDataProcessor


API = WeatherAPI()
PROCESSOR = WeatherDataProcessor()
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

class Command(BaseCommand):

    help = """Fetches the data from -->
              https://www.metoffice.gov.uk/climate/uk/summaries/datasets#Yearorder
              and stores it to database"""

    def add_arguments(self, parser):

        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            help='Fetches data for all regions',
        )

        parser.add_argument(
            '--regions',
            nargs='+',
            type=str,
            help='Provide the list of regions for which you want to populate data',
        )

    def handle(self, *args, **options):

        regions = []

        if options['all']:
            regions = Region.objects.all()
        elif options['regions']:
            regions = Region.objects.filter(name__in=options['regions'])

        if regions:
            for region in regions:
                self._process_region(region)
        else:
            raise CommandError("""Need regions to run or specify --all
                                  option to fetch all the regions""")

    def _process_region(self, region):

        try:
            raw_data = API.get_data(region.name)
            data = PROCESSOR.process_raw_data(raw_data)
            self._save_data(region, data)
        except RequestFailedException as e:
            LOGGER.error(e.message)

    def _save_data(self, region, data):

        with transaction.atomic():
            for date, value in data.items():

                try:
                    weather_obj = MonthlyWeather.objects.get(region=region,
                                                             month=date.month,
                                                             year=date.year)
                except MonthlyWeather.DoesNotExist:
                    weather_obj = MonthlyWeather(region=region,
                                                 month=date.month,
                                                 year=date.year)

                weather_obj.max_temperature = value['max_temperature']
                weather_obj.min_temperature = value['min_temperature']
                weather_obj.mean_temperature = value['mean_temperature']
                weather_obj.rainfall = value['rainfall']
                weather_obj.sunshine = value['sunshine']
                weather_obj.save()