# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import logging
import datetime
from WeatherPollution.models import Weather as wq
from WeatherPollution import csvValidation
import csv;
import urllib.request
import os
from django.utils.timezone import make_aware
# Setting up logging
logging.basicConfig(filename='WeatherPollution/logs/view.log', level=logging.DEBUG)


def pull_weather_csv(csv_file):
    try:
        print('Beginning file download with urllib2...')
        url = 'https://www.met.ie/latest-reports/observations/download'
        urllib.request.urlretrieve(url, csv_file)

    except IOError as e:
        print(e)
        print("IO Error in get weather CSV")


def pushNewData():
    # print the keys and values
    old_file_path = 'D:/Trinity_DS/AdvancedSoftwareEngineernig/Project/Sustainable_City_Management/WeatherPollution/CSV/weather_old.csv'
    new_csv_file  = 'D:/Trinity_DS/AdvancedSoftwareEngineernig/Project/Sustainable_City_Management/WeatherPollution/CSV/weather_new.csv'
    fileExists = os.path.isfile(old_file_path)
    if fileExists == False:
        pull_weather_csv(old_file_path)
        writeDatatoPostgres(old_file_path)
    else:
        pull_weather_csv(new_csv_file)
        if csvValidation.csv_update_validate(old_file_path,new_csv_file) == False:
            writeDatatoPostgres(new_csv_file)
            pull_weather_csv(old_file_path)
        else:
            print("No change in file so no write operation required")
def writeDatatoPostgres(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        last_update = datetime.datetime.now()
        for row in reader:
            Station = row['Station']
            Temperature = row['Temperature (ÂºC)']
            Weathercol = row['Weather']
            windspeed = row['Wind Speed (Kts)']
            windgust = row['Wind Gust (Kts)']
            winddirection = row['Wind Direction']
            humidity = row['Humidity (%)']
            rainfall = row['Rainfall (mm)']
            pressure=row['Pressure (hPa)']

            if Station == '-' or Station == 'n/a' or Station == "":
                Station = None
            if Temperature == '-' or Temperature == 'n/a' or Temperature == "":
                Temperature = None
            if Weathercol == '-' or Weathercol == 'n/a' or Weathercol == "":
                Weathercol = None
            if windspeed == '-' or windspeed == 'n/a' or windspeed == "":
                windspeed = None
            if windgust == '-'  or windgust == 'n/a' or windgust == "":
                windgust = None
            if winddirection == '-' or winddirection == 'n/a' or winddirection == "":
                winddirection = None
            if humidity == '-' or humidity == 'n/a' or humidity == "":
                humidity = None
            if rainfall == '-' or rainfall == 'n/a' or rainfall == "":
                rainfall = None
            if pressure == '-' or pressure == 'n/a' or pressure == "":
                pressure = None
            Weather = wq.objects.create(Station = Station,
                                    Temperature = Temperature,
                                    Weathercol = Weathercol,
                                    windspeed = windspeed,
                                    windgust = windgust,
                                    winddirection = winddirection,
                                    humidity = humidity,
                                    rainfall = rainfall,
                                    pressure = pressure,
                                    last_update=last_update)
            #print(Weather)
            Weather.save()

def index(request):
    pushNewData()
    latest_question_list = []
    template = loader.get_template('WeatherPollution/index.html')
    context = {
       'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

