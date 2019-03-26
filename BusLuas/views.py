from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from BusLuas.models import BusLuas as IrishRail
from django.http import JsonResponse
from APIHandling import DublinBusAPI


def index(request):
    template = loader.get_template('BusLuas/IrishRail.html')
    return HttpResponse(template.render())


def irishrail_data(request):
    template = loader.get_template('IrishRail.html')
    return HttpResponse(template.render())


def IrishRailData(request):
    # vsar data=CityEvents.objects.values_list('nametext', 'startutc', named=True)
    queryset = list(IrishRail.objects.filter().values())
    #print(queryset)
    return JsonResponse(queryset, safe=False)

def DublinBusData(request):
    print('Testthe----------------')
    test=DublinBusAPI.getAllDublinBusStandInfo()
    queryset = list(IrishRail.objects.filter().values())
    #print(queryset)
    return JsonResponse(queryset, safe=False)