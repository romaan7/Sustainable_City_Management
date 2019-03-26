# import xml.l.ElementTree as ET
import requests
from xmltodict import parse, ParsingInterrupted
import xml.etree.ElementTree as ET
import json


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
    for child in xml.iter('*'):
        if ("StopNumber" in child.tag):
            stationDetails["StopNumber"] = child.text
            
        if ("Longitude" in child.tag):
            
            stationDetails["Longitude"] = child.text
        if ("Latitude" in child.tag):
            
            stationDetails["Latitude"] = child.text
        if ("Description" in child.tag):
            
            stationDetails["Description"] = child.text
        json_response.append(stationDetails)
    

    # while {} in json_response:
    #     json_response.remove({})

    dump = json.dumps(json_response)
    responce = json.loads(dump)
    
    print('face')
    return dump

