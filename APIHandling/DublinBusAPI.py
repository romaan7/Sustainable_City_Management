# import xml.l.ElementTree as ET
import requests
from xmltodict import parse, ParsingInterrupted
import xml.etree.ElementTree as ET
import json
import xmltodict


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

