from django.urls import path

from . import views

app_name = 'CityEvents'
urlpatterns = [
    path('', views.index, name='index'),
]
