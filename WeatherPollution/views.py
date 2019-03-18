# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
import datetime
from WeatherPollution.models import Weather as wq
import json
from APIHandling import WeatherPollutionAPI
from django.db.models import Q


def writeDatatoPostgres(csv_to_json):
        reader = json.loads(csv_to_json)
        last_update = datetime.datetime.now()
        for row in reader:
            Station = row['Station']
            Temperature = row['Temperature']
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
            if windgust == '-' or windgust == 'n/a' or windgust == "":
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
            Weather.save()


def index(request):
    latest_csv, csv_flag = WeatherPollutionAPI.pull_weather_csv()
    csv_to_json = WeatherPollutionAPI.csv_to_json(latest_csv)
    print(csv_flag)
    if csv_flag:
        writeDatatoPostgres(csv_to_json)
    latest_question_list = []
    template = loader.get_template('WeatherPollution/index.html')
    context = {
       'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def weatherData(request):
    max_date = wq.objects.latest('last_update').last_update
    queryset = list(wq.objects.filter(Q(Station='Dublin') & Q(last_update__day=max_date.day)).values())
    print("##################################################QueryOutput###################################")
    print(queryset)
    print(max_date.second)
    print("##################################################QueryOutput###################################")
    '''
    wq.objects.filter(Station='Dublin').values()
    max_year = Expo.objects.latest('date').date.year
    expos = Expo.objects.filter(date__year=max_year)
    '''
    # data = CityEvents.objects.all()
    #print(queryset)
    return JsonResponse(queryset, safe=False)


def interactiveLine(request):

    template = loader.get_template('WeatherPollution/interactiveLine.html')

    context = {
       'data': [],
    }
    return HttpResponse(template.render(context, request))