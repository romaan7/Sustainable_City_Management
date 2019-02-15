from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from Bike.models import Bike
import datetime
from APIHandling import callJcdecauxAPI
from django.http import JsonResponse

def pushNewData():
    data = callJcdecauxAPI.getLatestData()
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

        b = Bike.objects.create(number=number, contract_name=contract_name, name=name, address=address,
                                position_lat=position_lat, position_lng=position_lng, banking=banking,
                                bonus=bonus, bike_stands=bike_stands, available_bike_stands=available_bike_stands,
                                available_bikes=available_bikes, status=status, last_update=last_update)
        b.save()

def index(request):
    #pushNewData()
    bike_data = []
    template = loader.get_template('bike.html')
    context = {
        'data': bike_data,
    }
    return HttpResponse(template.render(context, request))

def bike_data(request):
    data =  callJcdecauxAPI.getLatestData()
    return JsonResponse(list(data), safe=False)
