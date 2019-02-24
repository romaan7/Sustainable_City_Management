import xml.etree.ElementTree as ET
import requests

global station_code

def getTrainStationCodes():
     r = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')
     root = ET.fromstring(r.content)
     station_code=[]
     for child in root.iter('*'):
      if("StationCode" in child.tag):
        if(requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode='+child.text.strip()+'&NumMins=5').content):
          station_code += ['http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode='+child.text.strip()+'&NumMins=5']
     return(station_code)

