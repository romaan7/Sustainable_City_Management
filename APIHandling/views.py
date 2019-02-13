from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests
import logging
import json
from APIHandling.models import Bike as Bikeq
import datetime
from APIHandling import callJcdecauxAPI

# Setting up logging
logging.basicConfig(filename='APIHandling/logs/api_caller.log', level=logging.DEBUG)

def pushNewData():
    print('hi')
    data = callJcdecauxAPI.getLatestData()
    print(data)
    # print the keys and values
    for row in data:
        for key in row:
            number = row['number']
            contract_name = row['contract_name']
            name = row['name']
            address = row['address']
            position_lat = row['position']['lat']
            position_lng = row['position']['lng']
            banking = row['banking']
            bonus = row['bonus']
            bike_stands = row['bike_stands']
            available_bike_stands = row['available_bike_stands']
            available_bikes = row['available_bikes']
            status = row['status']
            last_update = datetime.datetime.fromtimestamp(int(str(row['last_update'])[:10]))

        Bike = Bikeq.objects.create(number=number, contract_name=contract_name, name=name, address=address,
                                position_lat=position_lat, position_lng=position_lng, banking=banking,
                                bonus=bonus, bike_stands=bike_stands, available_bike_stands=available_bike_stands,
                                    available_bikes=available_bikes, status=status, last_update=last_update)
        Bike.save()

def index(request):
    pushNewData()
    latest_question_list = []
    template = loader.get_template('APIHandling/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
