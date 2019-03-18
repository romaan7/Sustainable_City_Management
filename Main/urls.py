from django.urls import path

from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_2', views.index_2, name ='index_2'),
    path('index_3', views.index_3, name ='index_3'),
    path('index_4', views.index_4, name ='index_4'),
    path('index_5', views.index_5, name ='index_5'),
    path('send_city_json', views.send_city_json, name='send_city_json'),
    path('send_bike_json', views.send_bike_json, name='send_bike_json'),
    path('send_rail_json', views.send_rail_json, name='send_rail_json'),
]
