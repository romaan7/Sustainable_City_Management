# import xml.l.ElementTree as ET
import requests
from xmltodict import parse, ParsingInterrupted
import xml.etree.ElementTree as ET
import json
import xmltodict
from BusLuas.models import DublinBusStopData
from datetime import datetime

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
    print('InsideRealTime')
    dublinBusStop=list(DublinBusStopData.objects.filter()) 
    for f in dublinBusStop:
        print (f.BusStopNumber)
    
    url = "http://rtpi.dublinbus.ie/DublinBusRTPIService.asmx"

    querystring = {"WSDL":""}

    payload = "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:dub=\"http://dublinbus.ie/\">\r\n   <soap:Header/>\r\n   <soap:Body>\r\n      <dub:GetRealTimeStopData>\r\n         <dub:stopId>"+ str(1358)+"</dub:stopId>\r\n      </dub:GetRealTimeStopData>\r\n   </soap:Body>\r\n</soap:Envelope>"
    headers = {
        'Content-Type': "text/xml",
        'cache-control': "no-cache",
        'Postman-Token': "618820e6-6411-40c5-805a-9846f9812b55"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    stopDataRealTime=jsonResponse(response.text)
    finalData = {}
    # data['key'] = 'value'
    # json_data = json.dumps(data)
    for arr in stopDataRealTime:
        # print(arr)
        timeDiff=datetime.strptime(arr[:-6],'%Y-%m-%dT%H:%M:%S')-datetime.now()
        if(timeDiff.seconds<300):
            finalData['StopId']=312
            finalData['Zone']='Zone'
            finalData['Route']='Route'
            finalData['TimeId']=''

            print('true')
        else:
            break
        #if difference is less than 5 than insert into t
        # data = {}
        # data['key'] = 'value'
        # json_data = json.dumps(data)

    print('before ')
    # print(stopDataRealTime)
    # data = {}
    # data['key'] = 'value'
    # json_data = json.dumps(data)
    #getAllbusStopData()
    #loop and delay the call

    # url = "http://rtpi.dublinbus.ie/DublinBusRTPIService.asmx"
    # querystring = {"WSDL":""}
    # payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:dub=\"http://dublinbus.ie/\">\r\n   <soapenv:Header/>\r\n   <soapenv:Body>\r\n      <dub:GetAllDestinations/>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>"
    # headers = {
    #     'Content-Type': "text/xml",
    #     'cache-control': "no-cache",
    #     'Postman-Token': "b917a9d8-0e91-4578-a9c4-2c967dd4dcfa"
    #     }
    # response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    # json_response=[]
    # stationDetails={}
    # xml = ET.fromstring(response.text)
    # o = xmltodict.parse(response.text)
    # # print(json.dumps(o["soap:Envelope"]["soap:Body"]["GetAllDestinationsResponse"]["GetAllDestinationsResult"]["Destinations"]["Destination"]))
    # count=0
    # # for child in xml.iter('*'):
    # #     # print(child)
    # #     count=count+1
    # #     if ("StopNumber" in child.tag):
    # #         stationDetails["StopNumber"] = child.text
    # #         # print(child.text)
            
    # #     if ("Longitude" in child.tag):
            
    # #         stationDetails["Longitude"] = child.text
    # #         # print(child.text)
    # #     if ("Latitude" in child.tag):
            
    # #         stationDetails["Latitude"] = child.text
    # #     if ("Description" in child.tag):
            
    # #         stationDetails["Description"] = child.text
    # #     # print(stationDetails)
    # # json_response.append(stationDetails)    
    

    # # while {} in json_response:
    # #     json_response.remove({})
    # # print(json_response)
    # dump = json.dumps(json.dumps(o["soap:Envelope"]["soap:Body"]["GetAllDestinationsResponse"]["GetAllDestinationsResult"]["Destinations"]["Destination"]))
    

    # # print(dump)
    # responce = json.loads(dump)
    # # print(responce)
    
    # print('face')
    return ''

def jsonResponse(xmlText):
    

    o = xmltodict.parse(xmlText)
    print(o)
    response=json.loads(json.dumps(o['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    stopDataRealTime=json.loads(json.dumps(o['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    print('recieved')
    print(stopDataRealTime)
    dataArray=[]

    for element in stopDataRealTime:
        # print(json.dumps(element))
        dataArray.append(element['MonitoredCall_ExpectedDepartureTime'])
        print(element['MonitoredCall_ExpectedDepartureTime'])
    # print(stopDataRealTime)
    # print(type(response['soap:Envelope']["soap:Body"]["GetRealTimeStopDataResponse"]["GetRealTimeStopDataResult"]["diffgr:diffgram"]["DocumentElement"]["StopData"]))
    return dataArray