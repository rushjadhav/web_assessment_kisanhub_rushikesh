from django.conf.urls import url, include

from rest_framework import routers

from weather_data.views import *
from weather_data.api import *

router = routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'monthly_weathers', MonthlyWeatherViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^api/interesting_facts/$', InterstingFactsView.as_view(), name="facts"),
    url(r'^api/download/(?P<region_id>\d+)/$', DownloadRegionWeatherDataView.as_view(), name="download_data"),
    url(r'^api/', include(router.urls)),
]
