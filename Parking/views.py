from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from APIHandling import CustomUtil
from .models import carparkData

def index(request):
    template = loader.get_template('Parking/Parking.html')
    return HttpResponse(template.render())

def parking_data(request):
    q = carparkData.objects.all().values()
    json_object = CustomUtil.query_to_json(q)
    return JsonResponse(json_object, safe=False)
