from django.urls import path

from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.index, name='index'),
    path('DublinBikes', views.DublinBikes, name ='DublinBikes'),
    path('IrishRail', views.IrishRail, name ='IrishRail'),
    path('CityEvents', views.CityEvents, name ='CityEvents'),
    path('Weather', views.Weather, name ='Weather'),
    path('CarPark', views.CarPark, name ='CarPark'),
    path('send_city_json', views.send_city_json, name='send_city_json'),
    path('send_bike_json', views.send_bike_json, name='send_bike_json'),
    path('send_rail_json', views.send_rail_json, name='send_rail_json'),
    path('send_weather_json', views.send_weather_json, name='send_weather_json'),
]
