"""
Data processing layer converts api data to required format
"""

import datetime

from weather_data.utils import get_date_from_year_month

class WeatherDataProcessor(object):
    """
    Class Responsible for parsing data
    from raw data taken from metoffice
    """

    def _process_data(self, data):
        """
        """

        processed_data = {}

        for line in data:
            data = line.split()
            year = int(data[0])
            months = [get_date_from_year_month(month, year) for month in range(1, 13)]
            months_data = map(float, data[1:13])
            data = dict(zip(months, months_data))
            processed_data.update(data)
        return processed_data

    def _merge_data(self, max_temperatures, min_temperatures, mean_temperatures,
                    rainfall, sunshine):

        data = {}
        for key in max_temperatures.keys():
            data[key] = {
                'max_temperature': max_temperatures.get(key),
                'min_temperature': min_temperatures.get(key),
                'mean_temperature': mean_temperatures.get(key),
                'rainfall': rainfall.get(key),
                'sunshine': sunshine.get(key, 0.0),
            }
        return data

    def process_raw_data(self, raw_data):
        """
        Parse raw data and returns data in dictionary format.
        """

        max_temperatures = self._process_data(raw_data['max_temperatures'].splitlines()[8:])
        min_temperatures = self._process_data(raw_data['min_temperatures'].splitlines()[8:])
        mean_temperatures = self._process_data(raw_data['mean_temperatures'].splitlines()[8:])
        rainfall = self._process_data(raw_data['rainfall'].splitlines()[8:])
        sunshine = self._process_data(raw_data['sunshine'].splitlines()[8:])

        return self._merge_data(max_temperatures, min_temperatures, mean_temperatures,
                                rainfall, sunshine)
