from django.template.response import TemplateResponse
from django.shortcuts import render
import requests


from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from CityEvents.models import CityEvents
import datetime
from APIHandling import DublinBikesAPI
from django.http import JsonResponse
from APIHandling import CityEventAPI
import json


def index(request):

    template = loader.get_template('CityEvents/Calendar.html')
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))


def EventsPerWeek(request):
    cityEventData = CityEventAPI.getEventsPerWeek()
    # # # for target_list in cityEventData['events']:
    # # # eventsDataList=getEventsData()
    template = loader.get_template('CityEvents/EventsPerWeek.html')

    for target_list in cityEventData['events']:
        # status= target_list['status']
        descriptionText=target_list['description']['text']
        nametext=target_list['name']['text']
        organization_id =int(target_list['organization_id'])
        # online_event=target_list['online_event']
        startutc=target_list['start']['utc']
        endutc=target_list['end']['utc']
        listed=target_list['listed']
        is_free=target_list['is_free']
        url=target_list['url']
        # resource_uri=target_list['resource_uri']

        cityEvent=CityEvents.objects.create(nametext=nametext,organization_id=organization_id,listed=listed ,is_free=is_free,url=url,startutc=startutc,endutc=endutc)
        cityEvent.save()
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))

def MonthView(request):
    template = loader.get_template('CityEvents/MonthView.html')
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))

def CityEventData(request):
    # vsar data=CityEvents.objects.values_list('nametext', 'startutc', named=True)
    queryset = list(CityEvents.objects.filter().values())
    # data = CityEvents.objects.all()
    return JsonResponse(queryset, safe=False)


def ListEventData(request):
    template = loader.get_template('CityEvents/animations.html')
    queryset = list(CityEvents.objects.filter().values())
    print(queryset)
    #list = ['Bern','Bob','Eufronio','Epifanio','El pug']
    response = TemplateResponse(request, 'CityEvents/animations.html', {'eventList':queryset})
    context = {
        'data': [],
    }
    # return HttpResponse(template.render(context, request))
    return response


