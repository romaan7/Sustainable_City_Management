from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from datetime import timedelta
from APIHandling import CustomUtil
from .models import carparkData
from django.utils import timezone

def index(request):
    template = loader.get_template('Parking/Parking.html')
    return HttpResponse(template.render())

def parking_data(request):
    # this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
    # print("hr")
    # print(this_hour)
    # one_hour_later = this_hour + timedelta(hours=1)
    # print("hr2")
    # print(one_hour_later)
    # q = carparkData.objects.filter(cm_last_insert_dttm__range=(this_hour, one_hour_later)).values()
    # json_object = CustomUtil.query_to_json(q)
    # return JsonResponse(json_object, safe=False)

    #######
    this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
    print("hr")
    print(this_hour)
    one_hour_later = this_hour + timedelta(hours=1)
    print("hr2")
    print(one_hour_later)
    q = carparkData.objects.values().order_by('-id')[:14]
    print("q")
    print(q)
    json_object = CustomUtil.query_to_json(q)
    return JsonResponse(json_object, safe=False)


def parking_stats(request):
    template = loader.get_template('Parking/parking_stats.html')
    return HttpResponse(template.render())


def parking_statsdata(request):
        this_hour1 = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        print("hr1")
        print(this_hour1)
        one_hour_later1 = this_hour1 + timedelta(hours=24)
        print("hr21")
        print(one_hour_later1)
        q1 = carparkData.objects.values().order_by('-id')[:14]
        json_object1 = CustomUtil.query_to_json(q1)
        return JsonResponse(json_object1, safe=False)
