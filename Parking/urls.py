from django.urls import path

from . import views

app_name = 'Parking'
urlpatterns = [
    path('', views.index, name='index'),
    path('parking_data', views.parking_data, name='parking_data'),
]