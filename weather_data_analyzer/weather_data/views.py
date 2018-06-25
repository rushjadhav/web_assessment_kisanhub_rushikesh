# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from weather_data.models import Region, MonthlyWeather

class IndexView(View):
    """
    Class based view for index page
    """

    def get(self, request):

        regions = Region.objects.all()
        available_years = list(set(MonthlyWeather.objects.values_list('year', flat=True)))

        region_id = request.GET.get('region_id')

        if region_id:
            region = get_object_or_404(Region, pk=region_id)
        else:
            region = regions[0]

        average_max_temperature = region.get_average_max_temperature_monthwise()
        average_min_temperature = region.get_average_min_temperature_monthwise()
        average_mean_temperature = region.get_average_mean_temperature_monthwise()
        average_rainfall = region.get_average_rainfall_monthwise()
        average_sunshine = region.get_average_sunshine_monthwise()

        return render(request, "index.html",
            {'regions': regions,
             'average_sunshine': average_sunshine,
             'average_max_temperature': average_max_temperature,
             'average_min_temperature': average_min_temperature,
             'average_mean_temperature': average_mean_temperature,
             'average_rainfall': average_rainfall,
             'average_sunshine': average_sunshine,
             'current_region': region
            }) 