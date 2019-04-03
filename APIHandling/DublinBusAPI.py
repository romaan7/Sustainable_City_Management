# import xml.l.ElementTree as ET
import requests
from xmltodict import parse, ParsingInterrupted
import xml.etree.ElementTree as ET
import json
import xmltodict
from BusLuas.models import DublinBusStopData
from datetime import datetime
from BusLuas.models import DublinBusStopZoneData
from django.utils.timezone import make_aware
from django.utils import timezone

global station_code

def getAllDublinBusStandInfo():

    import requests
    url = "http://rtpi.dublinbus.ie/DublinBusRTPIService.asmx"
    querystring = {"WSDL":""}
    payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:dub=\"http://dublinbus.ie/\">\r\n   <soapenv:Header/>\r\n   <soapenv:Body>\r\n      <dub:GetAllDestinations/>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>"
    headers = {
        'Content-Type': "text/xml",
        'cache-control': "no-cache",
        'Postman-Token': "b917a9d8-0e91-4578-a9c4-2c967dd4dcfa"
        }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    json_response=[]
    stationDetails={}
    xml = ET.fromstring(response.text)
    o = xmltodict.parse(response.text)
    # print(json.dumps(o["soap:Envelope"]["soap:Body"]["GetAllDestinationsResponse"]["GetAllDestinationsResult"]["Destinations"]["Destination"]))
    count=0
    # for child in xml.iter('*'):
    #     # print(child)
    #     count=count+1
    #     if ("StopNumber" in child.tag):
    #         stationDetails["StopNumber"] = child.text
    #         # print(child.text)
            
    #     if ("Longitude" in child.tag):
            
    #         stationDetails["Longitude"] = child.text
    #         # print(child.text)
    #     if ("Latitude" in child.tag):
            
    #         stationDetails["Latitude"] = child.text
    #     if ("Description" in child.tag):
            
    #         stationDetails["Description"] = child.text
    #     # print(stationDetails)
    # json_response.append(stationDetails)    
    

    # while {} in json_response:
    #     json_response.remove({})
    # print(json_response)
    dump = json.dumps(json.dumps(o["soap:Envelope"]["soap:Body"]["GetAllDestinationsResponse"]["GetAllDestinationsResult"]["Destinations"]["Destination"]))
    

    # print(dump)
    responce = json.loads(dump)
    # print(responce)
    
    print('face')
    return responce

def getRealTimeDublinBusStandData():

    import requests
    
    dublinBusStop=list(DublinBusStopData.objects.filter()) 
    dublinBusStopZoneData=list(DublinBusStopZoneData.objects.filter()) 
    if(len(dublinBusStopZoneData)>0):
        DublinBusStopZoneData.objects.all().delete()
        for f in dublinBusStop:
            print (f.BusStopNumber)

            # f.BusStopNumber='1358'
            url = "http://rtpi.dublinbus.ie/DublinBusRTPIService.asmx"

            querystring = {"WSDL":""}

            payload = "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:dub=\"http://dublinbus.ie/\">\r\n   <soap:Header/>\r\n   <soap:Body>\r\n      <dub:GetRealTimeStopData>\r\n         <dub:stopId>"+f.BusStopNumber+"</dub:stopId>\r\n      </dub:GetRealTimeStopData>\r\n   </soap:Body>\r\n</soap:Envelope>"
            headers = {
                'Content-Type': "text/xml",
                'cache-control': "no-cache",
                'Postman-Token': "618820e6-6411-40c5-805a-9846f9812b55"
                }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

            stopDataRealTime,stopRouteId=jsonResponse(response.text)
            finalData={}
        # data['key'] = 'value'
        # json_data = json.dumps(data)
            try:
                for busTime,BusRoute in zip(stopDataRealTime,stopRouteId):
                    # print(arr)
                    timeDiff=datetime.strptime(busTime[:-6],'%Y-%m-%dT%H:%M:%S')-datetime.now()
                    if(timeDiff.seconds<300):
                        print('inside')
                        finalData['BusStopNumber']=f.BusStopNumber
                        finalData['BusStopZone']=f.BusStopZone
                        finalData['BusStopRoute']=BusRoute
                        finalData['BusStopIncomingTime']=stopDataRealTime
                        current_dttm = datetime.now(tz=timezone.utc)
                        cm_last_insert_dttm = current_dttm
                        cityEvent = DublinBusStopZoneData.objects.create(BusStopNumber=finalData['BusStopNumber'], BusStopZone=f.BusStopZone, BusStopRoute=BusRoute,
                                                            BusStopIncomingTime=busTime,
                                                            cm_last_insert_dttm=cm_last_insert_dttm)

                        print('true--------------------')
                    else:
                        break
                    #if difference is less than 5 than insert into t
                    # data = {}
                    # data['key'] = 'value'
                    # json_data = json.dumps(data)
            except:
                #print(stopDataRealTime)
                pass
    return ''

def jsonResponse(xmlText):
    
    o = xmltodict.parse(xmlText)
    # print(o)
    # stopDataRealTime=json.loads(json.dumps(o['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))

    print('///////////////////////////////////')
    dataArray=[]
    dataRoute=[]
    # dataArray.append(stopDataRealTime['MonitoredCall_ExpectedDepartureTime'])
    # dataRoute.append(stopDataRealTime['MonitoredVehicleJourney_PublishedLineName'])
    try:
        stopDataRealTime=json.loads(json.dumps(o['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
        if len(stopDataRealTime)==1:
            pass
        elif len(stopDataRealTime)==2:
            dataArray.append(stopDataRealTime['MonitoredCall_ExpectedDepartureTime'])
            dataRoute.append(stopDataRealTime['MonitoredVehicleJourney_PublishedLineName'])
        else:
            for element in stopDataRealTime:
           # print(json.dumps(element))
                dataArray.append(element['MonitoredCall_ExpectedDepartureTime'])
                dataRoute.append(element['MonitoredVehicleJourney_PublishedLineName'])
            
    except:
        #print(stopDataRealTime)
        pass
        # print(element['MonitoredCall_ExpectedDepartureTime'])
    # print(stopDataRealTime)
    # print(type(response['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    return dataArray,dataRoute