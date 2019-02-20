from django.urls import path

from . import views

app_name = 'WeatherPollution'
urlpatterns = [
    path('', views.index, name='index'),
    path('WeatherPollution', views.index, name='WeatherPollution'),
]