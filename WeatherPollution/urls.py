from django.urls import path

from . import views

app_name = 'WeatherPollution'
urlpatterns = [
    path('WeatherPollution', views.index, name='index'),
]