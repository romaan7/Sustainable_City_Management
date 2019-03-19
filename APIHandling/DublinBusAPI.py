import xml.l.ElementTree as ET
import requests

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
    print(response.text)
    return response.text

