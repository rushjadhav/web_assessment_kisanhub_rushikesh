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

    def get_data(self, region_name='UK'):
        """
        region_name: String, e.g. UK, England
        """

        #Max Temperature
        max_temperatures = self._make_request("Tmax/date/{0}.txt".format(region_name))

        #Min Temperature
        min_temperatures = self._make_request("Tmin/date/{0}.txt".format(region_name))

        #Mean Temperature
        mean_temperatures = self._make_request("Tmean/date/{0}.txt".format(region_name))

        #Rainfall
        rainfall = self._make_request("Rainfall/date/{0}.txt".format(region_name))

        #Sunshine
        sunshine = self._make_request("Sunshine/date/{0}.txt".format(region_name))

        return {
            'max_temperatures': max_temperatures,
            'min_temperatures': min_temperatures,
            'mean_temperatures': mean_temperatures,
            'rainfall': rainfall,
            'sunshine': sunshine
        }
