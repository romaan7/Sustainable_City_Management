from django.urls import path

from . import views

app_name = 'CityEvents'
urlpatterns = [
    path('', views.index, name='index'),
    path('EventsPerWeek', views.EventsPerWeek, name='EventsPerWeek'),
    path('MonthView', views.MonthView, name='MonthView'),
    path('CityEventData', views.CityEventData, name='CityEventData'),
    
]