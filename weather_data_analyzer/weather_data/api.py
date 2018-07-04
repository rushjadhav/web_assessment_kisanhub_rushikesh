import csv

from django.http import HttpResponse

from rest_framework import viewsets, views
from rest_framework.response import Response

from weather_data.utils import get_random_string, get_date_from_year_month
from weather_data.models import Region, MonthlyWeather
from weather_data.serializers import RegionSerializer, MonthlyWeatherSerializer

class InterstingFactsView(views.APIView):

    def get(self, request, format=None):

        interesting_facts = ["Scotland & Wales regions have almost identical data",
                             "Among the 4 regions england has less rainfall",
                             "Scotland is the coolest region in given four regions"]

        return Response(interesting_facts)

class DownloadRegionWeatherDataView(views.APIView):

    def get(self, request, region_id, format=None):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{0}.csv"'.format(get_random_string())
        rows = MonthlyWeather.objects.filter(region_id=region_id)
        self._write_csv(response, rows)
        return response

    def _write_csv(self, response, rows):
        writer = csv.writer(response)

        writer.writerow(["Month", "Max Temperature", "Min Temperature",
                            "Mean Temperature", "Rainfall", "Sunshine"])
        for row in rows:
            writer.writerow([get_date_from_year_month(row.month, row.year).strftime("%b %Y"),
                             row.max_temperature, row.min_temperature,
                             row.mean_temperature, row.rainfall, row.sunshine])


class RegionViewSet(viewsets.ModelViewSet):

    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class MonthlyWeatherViewSet(viewsets.ModelViewSet):
    queryset = MonthlyWeather.objects.all()
    serializer_class = MonthlyWeatherSerializer

    def get_queryset(self):

        query_dict = self._get_query_dict_from_query_params()

        if query_dict:
            data = MonthlyWeather.objects.filter(**query_dict)
        else:
            data = MonthlyWeather.objects.all()

        return data

    def _get_query_dict_from_query_params(self):

        region_id = self.request.query_params.get('region_id')
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        query_dict = {}
        if region_id:
            query_dict['region_id'] = int(region_id)
        if month:
            query_dict['month'] = int(month)
        if year:
            query_dict['year'] = int(year)
        return query_dict
