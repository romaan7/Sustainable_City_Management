from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from BusLuas.models import BusLuas as IrishRail
from BusLuas.models import DublinBusStopData
from django.http import JsonResponse
import xmltodict

import requests
import simplejson as json
# import json

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
    queryset = list(DublinBusStopData.objects.filter().values())
    #print(queryset)
    return JsonResponse(queryset, safe=False)

def RealTimeBusData(request):
    print(request.GET)
    print('----------------')
    # stopid = request.GET.get('stopnumber')
    stopid=request.GET['stopnumber']
    print(stopid)
    # stopid = request.form['stopid']
    # print(stopid)



    url = "http://rtpi.dublinbus.ie/DublinBusRTPIService.asmx"

    querystring = {"WSDL":""}

    payload = "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:dub=\"http://dublinbus.ie/\">\r\n   <soap:Header/>\r\n   <soap:Body>\r\n      <dub:GetRealTimeStopData>\r\n         <dub:stopId>"+ str(stopid)+"</dub:stopId>\r\n      </dub:GetRealTimeStopData>\r\n   </soap:Body>\r\n</soap:Envelope>"
    headers = {
        'Content-Type': "text/xml",
        'cache-control': "no-cache",
        'Postman-Token': "618820e6-6411-40c5-805a-9846f9812b55"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    # print(response.text)
    stopDataRealTime=jsonResponse(response.text)



    # dblink = 'http://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=' + str(stopid)+ '&format=json'
    # r = requests.get(dblink)
    # print(r)

    fileName=str(stopid)+ '.json'
    with open(fileName, 'w') as outfile:
        json.dump(stopDataRealTime, outfile)
    
    # jsondata = json.loads(r.text)
    # jsonpath = 'dbapp/static/json_data/stop' + str(stopid)+ '.json'
    # dir = os.path.dirname(jsonpath)
    # if not os.path.exists(dir):
    #     os.makedirs(dir)
    # with open(jsonpath, 'w') as f:
    #     json.dump(jsondata, f)
    print(type(stopDataRealTime))
    return JsonResponse(stopDataRealTime, safe=False) 


def jsonResponse(xmlText):
    print('recieved')

    o = xmltodict.parse(xmlText)
    print(o)
    response=json.loads(json.dumps(o['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    stopDataRealTime=json.loads(json.dumps(o['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    # print(stopDataRealTime)
    for element in stopDataRealTime:
        # print(json.dumps(element))
        print(element['MonitoredCall_ExpectedDepartureTime'])
    # print(stopDataRealTime)
    # print(type(response['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    return stopDataRealTime


def DublinBusSearchResult(request):
    print(request)
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        print('--------------------------------------------')
        print(q)
        test=list(DublinBusStopData.objects.filter(BusStopStationName__icontains=q))
        # print(test)
        # search_qs = DublinBusStopData.objects.filter()
        # print('search_qs')
        results = []
        for r in test:
            results.append(json.dumps({'StopName': r.BusStopStationName,'StationId':r.BusStopNumber,'lat':r.BusStopLatitude,'lng':r.BusStopLongitude},use_decimal=True ))
        # print(results)
        data = json.dumps(results)
        

    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)



# def BusDashBoard(request):
#     template = loader.get_template('DublinBus.html')
#     return HttpResponse(template.render())
