from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import logging
import datetime
from WeatherPollution.models import Weather as wq
import csv;
import urllib.request
# Setting up logging
logging.basicConfig(filename='WeatherPollution/logs/view.log', level=logging.DEBUG)


def pull_weather_csv(csv_file):
    try:
        print('Beginning file download with urllib2...')
        url = 'https://www.met.ie/latest-reports/observations/download'
        urllib.request.urlretrieve(url, csv_file)

    except IOError:
        print("IO Error in get weather CSV")


def pushNewData():
    # print the keys and values
    print("Tryinig------------")
    csv_file='D:\Trinity_DS\AdvancedSoftwareEngineernig\Project\Sustainable_City_Management\WeatherPollution\CSV/weather.csv'
    pull_weather_csv(csv_file)
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Station=row['Station']
            Temperature=row['Temperature (ÂºC)']
            Weathercol = row['Weather']
            windspeed = row['Wind Speed (Kts)']
            windgust = row['Wind Gust (Kts)']
            winddirection = row['Wind Direction']
            humidity = row['Humidity (%)']
            rainfall = row['Rainfall (mm)']
            pressure=row['Pressure (hPa)']

            print("########## Temperature ########## " + Temperature)
            if humidity == '-':
                print("True--------")
                humidity = 999
                print("########## humidity ##########"+humidity)
            if Temperature == '-':
                print("True--------")
                Temperature = 999
                print("########## humidity ##########" + Temperature)

            Weather = wq.objects.create(Station=Station,
                                    Temperature = Temperature,
                                    Weathercol = Weathercol,
                                    windspeed = windspeed,
                                    windgust = windgust,
                                    winddirection = winddirection,
                                    humidity = humidity,
                                    rainfall = rainfall,
                                    pressure = pressure)
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

