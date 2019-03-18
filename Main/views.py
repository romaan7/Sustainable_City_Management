from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from CityEvents import views as CityEvents
from Bike import views as Bike
from BusLuas import views as IrishRail
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
    
def send_city_json(request):
    data = (CityEvents.CityEventData(request))
    json_data = json.loads(data.content)
    #print(json_data)
    return JsonResponse(json_data, safe=False)

def send_bike_json(request):
    data = (Bike.bike_data(request))
    json_data = json.loads(data.content)
    print(json_data)
    return JsonResponse(json_data, safe=False)

def send_rail_json(request):
    data = (IrishRail.IrishRailData(request))
    json_data = json.loads(data.content)
    print(json_data)
    return JsonResponse(json_data, safe=False)
   
#print(CityEventData())
#def getWeatherUpdates():
#    data = DublinBikesAPI.getLatestData()
#    for row in data:
#        for key in row:
#            number = row['number']
#            contract_name = row['contract_name']
#            name = row['name']
#            address = row['address']
#            position_lat = row['position']['lat']
#            position_lng = row['position']['lng']
#            banking = row['banking']
#            bonus = row['bonus']
#            bike_stands = row['bike_stands']
#            available_bike_stands = row['available_bike_stands']
#            available_bikes = row['available_bikes']
#            status = row['status']
#            last_update = make_aware(datetime.datetime.fromtimestamp(int(str(row['last_update'])[:10])))

#        b = Bike.objects.create(number=number, contract_name=contract_name, name=name, address=address,
#                                position_lat=position_lat, position_lng=position_lng, banking=banking,
#                                bonus=bonus, bike_stands=bike_stands, available_bike_stands=available_bike_stands,
#                                available_bikes=available_bikes, status=status, last_update=last_update)
#        b.save()

#    return data