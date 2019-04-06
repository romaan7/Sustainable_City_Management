from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from CityEvents import views as CityEvents
from Bike import views as Bike
from BusLuas import views as IrishRail
from WeatherPollution import views as Weather
import json
import psycopg2.extras
import sys,os
import configparser
from psycopg2.extras import RealDictCursor


def getAnalyticsView():
    config = configparser.ConfigParser()
    CFG_DIR = os.path.join(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), '..'), 'config.ini')
    config.read(CFG_DIR)
    conn = psycopg2.connect(database=config.get('AWS', 'database'),
                            port=config.get('AWS', 'Port'),
                            user=config.get('USERS_CREDS', 'user'),
                            password=config.get('USERS_CREDS', 'pwd'), host=config.get('AWS', 'host'))
    cursor = conn.cursor('cursor_unique_name',
                         cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM public."real_time_analytics"')
    json_output =cursor.fetchall()
    return json_output

def RealTimeData(request):
    return JsonResponse(getAnalyticsView(), safe=False)

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


def BusDashBoard(request):
    template = loader.get_template('DublinBus.html')
    return HttpResponse(template.render({}, request))

def Analytics(request):
    template = loader.get_template('Analytics.html')
    return HttpResponse(template.render({}, request))

def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)

