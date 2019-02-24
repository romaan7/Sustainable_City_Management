from array import array

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from Parking.models import Parking as Parking1
from Parking import callAPI
from django.http import JsonResponse

from django.utils.timezone import make_aware
import datetime

import re

# Setting up logging
#logging.basicConfig(filename='APIHandling/logs/api_caller.log', level=logging.DEBUG)

def pushNewData():
#print('hi')
    data = callAPI.getLatestData()
#print(data)
    # print the keys and values
    for feature in data['features']:
       # for key in row:
        #    for key in row:
                coordinates = feature['geometry']['coordinates']
                Point = feature['geometry']['type']
                OBJECTID = feature['properties']['OBJECTID']
                id1 = feature['properties']['id']
                location = feature['properties']['location']
                noofspaces = feature['properties']['noofspaces']
                roadname = feature['properties']['roadname']
                spacetype = feature['properties']['spacetype']
                # last_update = format(datetime.datetime.now())

                #print(type(coordinates))
                #coord1 = coordinates.split(",")


                test1 = str(coordinates).strip('[]')
                coord1 = test1.split(",")
                lat = float(coord1[1])
                long = float(coord1[0])

                Parking = Parking1.objects.create(id1=id1, location=location, roadname=roadname, noofspaces=noofspaces,
                                          spacetype=spacetype, OBJECTID=OBJECTID, lat=lat, long=long,  Point= Point)

                Parking.save()
    return data

def index(request):
    pushNewData()
    latest_question_list = []
    template = loader.get_template('Parking/Parking.html')
    context = {
        'data': parking_data,
    }
    return HttpResponse(template.render(context, request))

def parking_data(request):
    print('test')
    data = pushNewData()
    print(data)
    return JsonResponse(data, safe=False)

# def parking_data(request):
#    #print('test')
#     data =pushNewData()
#  #print(data)
#     test=[]
#     return JsonResponse(data, safe=False)

