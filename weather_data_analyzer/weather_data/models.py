# -*- coding: utf-8 -*-
"""
Module contains daat models required for application
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):
    """
    class Represention a Region e.g. England, UK, Wales
    """

    name = models.CharField(_('Name'), max_length=255, unique=True, null=False, blank=False)

    def _get_average_value_monthly(self, field_name):
        response = []
        for month in range(1, 13):
            data = self.monthly_weather.filter(month=month).values_list(field_name, flat=True)
            data = sum(data)/len(data)
            response.append(round(data, 2))

        return response

    def get_average_max_temperature_monthwise(self):
        return self._get_average_value_monthly('max_temperature')

    def get_average_min_temperature_monthwise(self):
        return self._get_average_value_monthly('min_temperature')

    def get_average_mean_temperature_monthwise(self):
        return self._get_average_value_monthly('mean_temperature')

    def get_average_sunshine_monthwise(self):
        return self._get_average_value_monthly('sunshine')

    def get_average_rainfall_monthwise(self):
        return self._get_average_value_monthly('rainfall')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'region'


class MonthlyWeather(models.Model):
    """
    Class Representing a weather information for particular month
    """

    region = models.ForeignKey(Region, related_name="monthly_weather")

    max_temperature = models.FloatField(_('Max Temperature'), null=False, blank=False)

    min_temperature = models.FloatField(_('Min Temperature'), null=False, blank=False)

    mean_temperature = models.FloatField(_('Mean Temperature'), null=False, blank=False)

    sunshine = models.FloatField(_('Sunshine'), null=False, blank=False)

    rainfall = models.FloatField(_('Rainfall'), null=False, blank=False)

    year = models.IntegerField(null=False, blank=False)

    month = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "{0}({1}-{2})".format(self.region, self.month, self.year)

    class Meta:
        db_table = 'monthly_weather'
        unique_together = (('month', 'year', 'region'),)
        ordering = ['-year', '-month']
