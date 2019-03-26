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

def CityEventsAnimations(request):
    template = loader.get_template('CityEvents/animations.html')
    return HttpResponse(template.render({}, request))
   
def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

