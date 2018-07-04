"""
Weather API module for fetching data from metoffice site
"""

import requests

BASE_URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets"

class RequestFailedException(Exception):
    """
    Custom exception to raised when api fails
    """
    def __init__(self, status_code, error_message):
        super(RequestFailedException, self).__init__("""Cant make request!
                            Status code: {0},
                            Error Message: {1}""".format(status_code, error_message))

class WeatherAPI(object):
    """
    Class Responsible for downloading weather data from metoffice site
    """

    def __init__(self):

        self.base_url = BASE_URL

    def _make_request(self, relative_url):
        """
        Makes request to the given url.
        """

        url = "{0}/{1}".format(self.base_url, relative_url)

        response = requests.get(url)
        if int(response.status_code) == 200:
            return response.text
        else:
            raise RequestFailedException(response.status_code, response.text)

    def _get_relative_url(self, parameter_name, region_name):

        return "{0}/date/{1}.txt".format(parameter_name, region_name)

    def get_data(self, region_name='UK'):
        """
        region_name: String, e.g. UK, England
        """

        return {
            'max_temperatures': self._make_request(self._get_relative_url("Tmax", region_name)),
            'min_temperatures': self._make_request(self._get_relative_url("Tmin", region_name)),
            'mean_temperatures': self._make_request(self._get_relative_url("Tmean", region_name)),
            'rainfall': self._make_request(self._get_relative_url("Rainfall", region_name)),
            'sunshine': self._make_request(self._get_relative_url("Sunshine", region_name))
        }
