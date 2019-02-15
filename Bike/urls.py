from django.urls import path

from . import views

app_name = 'Bike'
urlpatterns = [
    path('', views.index, name='index'),
    path('bike_data', views.bike_data, name='bike_data'),
]