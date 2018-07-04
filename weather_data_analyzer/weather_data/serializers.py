from rest_framework import serializers

from weather_data.models import Region, MonthlyWeather

class RegionSerializer(serializers.HyperlinkedModelSerializer):

    average_max_temperature_monthwise = serializers.SerializerMethodField()

    average_min_temperature_monthwise = serializers.SerializerMethodField()

    average_mean_temperature_monthwise = serializers.SerializerMethodField()

    average_rainfall_monthwise = serializers.SerializerMethodField()

    average_sunshine_monthwise = serializers.SerializerMethodField()

    def get_average_max_temperature_monthwise(self, region):
        return region.get_average_max_temperature_monthwise()

    def get_average_min_temperature_monthwise(self, region):
        return region.get_average_min_temperature_monthwise()

    def get_average_mean_temperature_monthwise(self, region):
        return region.get_average_mean_temperature_monthwise()

    def get_average_sunshine_monthwise(self, region):
        return region.get_average_sunshine_monthwise()

    def get_average_rainfall_monthwise(self, region):
        return region.get_average_rainfall_monthwise()

    class Meta:
        model = Region
        fields = ('id', 'name', 'average_max_temperature_monthwise',
                  'average_min_temperature_monthwise', 'average_mean_temperature_monthwise',
                  'average_rainfall_monthwise', 'average_sunshine_monthwise')

class MonthlyWeatherSerializer(serializers.HyperlinkedModelSerializer):

    region_name = serializers.SerializerMethodField()

    def get_region_name(self, monthly_weather):
        return monthly_weather.region.name

    class Meta:
        model = MonthlyWeather
        fields = ('region', 'region_name', 'max_temperature', 'min_temperature',
                  'mean_temperature', 'sunshine', 'rainfall', 'year', 'month')
