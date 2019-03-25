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
    # q = carparkData.objects.all().values()
    # json_object = CustomUtil.query_to_json(q)
    # return JsonResponse(json_object, safe=False)
    this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
    print("hr")
    print(this_hour)
    one_hour_later = this_hour + timedelta(hours=1)
    print("hr2")
    print(one_hour_later)
    q = carparkData.objects.filter(cm_last_insert_dttm__range=(this_hour, one_hour_later)).values()
    json_object = CustomUtil.query_to_json(q)
    return JsonResponse(json_object, safe=False)
