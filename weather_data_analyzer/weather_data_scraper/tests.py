# -*- coding: utf-8 -*-
"""
Test cases for api and processor modules
"""

from __future__ import unicode_literals
import datetime

from django.test import TestCase

from weather_data_scraper.WeatherAPI import WeatherAPI, RequestFailedException
from weather_data_scraper.WeatherDataProcessor import WeatherDataProcessor

class TestWeatherAPI(TestCase):
    """
    Test cases for api class
    """

    def setUp(self):
        self.api = WeatherAPI()

    def test_get_data_with_invalid_region(self):
        response = self.api.get_data('England')
        self.assertNotEqual(response, None)

    def test_get_data_with_valid_region(self):
        with self.assertRaises(RequestFailedException):
            self.api.get_data('21323')

class TestWeatherDataProcessor(TestCase):
    """
    Test cases for processor class
    """

    def setUp(self):
        self.api = WeatherAPI()
        self.processor = WeatherDataProcessor()
        self.england_raw_data = self.api.get_data('England')

    def test_process_raw_data_for_max_temperature(self):

        date = datetime.datetime.strptime("05/1990", "%m/%Y")
        processed_data = self.processor.process_raw_data(self.england_raw_data)
        self.assertEqual(17.7, processed_data[date]['max_temperature'])

    def test_process_raw_data_for_min_temperature(self):
        date = datetime.datetime.strptime("05/1990", "%m/%Y")
        processed_data = self.processor.process_raw_data(self.england_raw_data)
        self.assertEqual(6.7, processed_data[date]['min_temperature'])

    def test_process_raw_data_for_mean_temperature(self):
        date = datetime.datetime.strptime("05/1990", "%m/%Y")
        processed_data = self.processor.process_raw_data(self.england_raw_data)
        self.assertEqual(12.2, processed_data[date]['mean_temperature'])

    def test_process_raw_data_for_rainfall(self):
        date = datetime.datetime.strptime("05/1990", "%m/%Y")
        processed_data = self.processor.process_raw_data(self.england_raw_data)
        self.assertEqual(22.4, processed_data[date]['rainfall'])

    def test_process_raw_data_for_sunshine(self):
        date = datetime.datetime.strptime("05/1990", "%m/%Y")
        processed_data = self.processor.process_raw_data(self.england_raw_data)
        self.assertEqual(244.4, processed_data[date]['sunshine'])
