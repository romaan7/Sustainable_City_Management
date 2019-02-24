import requests
import json

def getEventsPerWeek():
    url = "https://www.eventbriteapi.com/v3/events/search/"
    querystring = {"location.address": "Dublin", "start_date.range_start": "2019-02-18T16:22:00Z",
               "token": "DSL5CXCJDV7UDZLLMN7J"}
    response = requests.request("GET", url, params=querystring)
    city_event_data = json.loads(response.text)
    return city_event_data
