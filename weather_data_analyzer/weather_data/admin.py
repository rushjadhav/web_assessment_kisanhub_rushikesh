# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from weather_data.models import Region, MonthlyWeather

admin.site.register([Region, MonthlyWeather])
