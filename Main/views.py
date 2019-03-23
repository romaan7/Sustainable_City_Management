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
def DublinBikes(request):
    template = loader.get_template('DublinBikes.html')
    return HttpResponse(template.render({}, request))
def IrishRail(request):
    template = loader.get_template('IrishRail.html')
    return HttpResponse(template.render({}, request))
def CityEvents(request):
    template = loader.get_template('CityEvents.html')
    return HttpResponse(template.render({}, request))
def Weather(request):
    template = loader.get_template('Weather.html')
    return HttpResponse(template.render({}, request))
def CarPark(request):
    template = loader.get_template('CarPark.html')
    return HttpResponse(template.render({}, request))
    
def send_city_json(request):
    data = (CityEvents.CityEventData(request))
    json_data = json.loads(data.content)
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
   
def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

