from django.urls import path

from . import views

app_name = 'api_handling'
urlpatterns = [
    path('', views.index, name='index'),
]