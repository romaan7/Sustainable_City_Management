from django.shortcuts import render
import dateutil.parser
import datetime
from dateutil.parser import parse
from django.utils import formats
from django.utils import formats
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
import logging
import json
from BusLuas.models import BusLuas as IrishRail
from APIHandling import IrishRailAPI as IrishRailXML
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom
from xml.dom import minidom
import requests
from django.http import JsonResponse


def index(request):
    template = loader.get_template('BusLuas/IrishRail.html')
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))


def pushNewData():
    ServerTime = ''
    TrainCode = ''
    StationFullName = ''
    StationCode = ''
    QueryTime = ''
    Traindate = ''
    Origin = ''
    Destination = ''
    Origintime = ''
    Destinationtime = ''
    Status = ''
    Lastlocation = ''
    Duein = ''
    Late = ''
    Exparrival = ''
    Expdepart = ''
    Scharrival = ''
    Schdepart = ''
    Direction = ''
    Traintype = ''
    Locationtype = ''
    station_code = IrishRailXML.getTrainStationCodes()
    for item in station_code:
        r1 = requests.get(item)
        root_item = ET.fromstring(r1.content)
        for child in root_item.iter('*'):
            if ("Servertime" in child.tag):
                ServerTime = child.text
            if ("Traincode" in child.tag):
                TrainCode = child.text
            if ("Stationfullname" in child.tag):
                StationFullName = child.text
            if ("Stationcode" in child.tag):
                StationCode = child.text
            if ("Querytime" in child.tag):
                QueryTime = child.text + ":00"
            if ("Traindate" in child.tag):
                Traindate = child.text
            if ("Origin" in child.tag) and ("Origintime" not in child.tag):
                Origin = child.text
            if ("Destination" in child.tag) and ("Destinationtime" not in child.tag):
                Destination = child.text
            if ("Origintime" in child.tag):
                Origintime = child.text + ":00"
            if ("Destinationtime" in child.tag):
                Destinationtime = child.text + ":00"
            if ("Status" in child.tag):
                Status = child.text
            if ("Lastlocation" in child.tag):
                Lastlocation = child.text
            if ("Duein" in child.tag):
                Duein = child.text
            if ("Late" in child.tag):
                Late = child.text
            if ("Exparrival" in child.tag):
                Exparrival = child.text + ":00"
            if ("Expdepart" in child.tag):
                Expdepart = child.text + ":00"
            if ("Scharrival" in child.tag):
                Scharrival = child.text + ":00"
            if ("Schdepart" in child.tag):
                Schdepart = child.text + ":00"
            if ("Direction" in child.tag):
                Direction = child.text
            if ("Traintype" in child.tag):
                Traintype = child.text
            if ("Locationtype" in child.tag):
                Locationtype = child.text

                BusLuas = IrishRail.objects.create(ServerTime=ServerTime, TrainCode=TrainCode,
                                                   StationFullName=StationFullName, StationCode=StationCode,
                                                   QueryTime=QueryTime, Traindate=Traindate, Origin=Origin,
                                                   Destination=Destination, Origintime=Origintime,
                                                   Destinationtime=Destinationtime, Status=Status,
                                                   Lastlocation=Lastlocation, Duein=Duein, Late=Late,
                                                   Exparrival=Exparrival,
                                                   Expdepart=Expdepart, Scharrival=Scharrival, Schdepart=Schdepart,
                                                   Direction=Direction, Traintype=Traintype, Locationtype=Locationtype)
                BusLuas.save()
        context = {
            'data': [],
        }
    return HttpResponse(template.render(context, request))


def irishrail_data(request):
    template = loader.get_template('IrishRail.html')
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))


def IrishRailData(request):
    # vsar data=CityEvents.objects.values_list('nametext', 'startutc', named=True)
    queryset = list(IrishRail.objects.filter().values())
    #print(queryset)
    return JsonResponse(queryset, safe=False)
