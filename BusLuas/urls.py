from django.urls import path

from . import views

app_name = 'BusLuas'
urlpatterns = [
    path('', views.index, name='index'),
    path('IrishRailData', views.IrishRailData, name='IrishRailData'),
    path('DublinBusData', views.DublinBusData, name='DublinBusData'),
]   