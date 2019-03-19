from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from CityEvents import views as CityEvents
from Bike import views as Bike
from BusLuas import views as IrishRail
from WeatherPollution import views as Weather
import json
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
def index_2(request):
    template = loader.get_template('index_2.html')
    return HttpResponse(template.render({}, request))
def index_3(request):
    template = loader.get_template('index_3.html')
    return HttpResponse(template.render({}, request))
def index_4(request):
    template = loader.get_template('index_4.html')
    return HttpResponse(template.render({}, request))
def index_5(request):
    template = loader.get_template('index_5.html')
    return HttpResponse(template.render({}, request))
def index_6(request):
    template = loader.get_template('index_6.html')
    return HttpResponse(template.render({}, request))
    
def send_city_json(request):
    data = (CityEvents.CityEventData(request))
    json_data = json.loads(data.content)
    #print(json_data)
    return JsonResponse(json_data, safe=False)

def send_bike_json(request):
    data = (Bike.bike_data(request))
    json_data = json.loads(data.content)
    #print(json_data)
    return JsonResponse(json_data, safe=False)

def send_rail_json(request):
    data = (IrishRail.IrishRailData(request))
    json_data = json.loads(data.content)
    #print(json_data)
    return JsonResponse(json_data, safe=False)

def send_weather_json(request):
    data = (Weather.weatherData(request))
    json_data = json.loads(data.content)
    #print(json_data)
    return JsonResponse(json_data, safe=False)
