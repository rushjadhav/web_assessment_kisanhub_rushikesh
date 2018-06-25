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