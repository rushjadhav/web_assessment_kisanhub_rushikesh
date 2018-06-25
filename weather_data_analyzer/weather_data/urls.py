from django.conf.urls import url 

from weather_data.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
]
