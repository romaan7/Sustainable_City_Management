import urllib.request
import hashlib
import logging
import csv
import json
import time
import glob
import os

CURRENT_TIMESTAMP = time.strftime("%Y%m%d-%H%M%S")


def pull_weather_csv():
    csv_file_name = "./APIHandling/weather_files/weatherCSV-" + CURRENT_TIMESTAMP + ".csv"
    url = 'https://www.met.ie/latest-reports/observations/download'
    try:
        list_of_files = glob.glob('./APIHandling/weather_files/*.csv')
        if list_of_files:
            last_file = max(list_of_files, key=os.path.getctime)
            urllib.request.urlretrieve(url, csv_file_name)
            if csv_update_validate(last_file, csv_file_name):
                return csv_file_name
            else:
                print("The Downloaded file is same as old one. No need for newfile.Removing new file")
                os.remove(csv_file_name)
                return last_file
        else:
            urllib.request.urlretrieve(url, csv_file_name)
            return csv_file_name
    except IOError as e:
        logging.exception('I/O Error with CSV file ' + str(e))
        raise e

def csv_to_json(csv_file):
    f = open(csv_file, 'r')
    reader = csv.DictReader(f, fieldnames=("Station", "Temperature", "Weather",
                                           "Wind Speed (Kts)", "Wind Gust (Kts)", "Wind Direction", "Humidity (%)",
                                           "Rainfall (mm)", "Pressure (hPa)"))
    next(reader, None)#skips the header row
    nice_json = json.dumps([row for row in reader])
    return nice_json



def csv_update_validate(old_csv_file,new_csv_file):
    if SHA256(old_csv_file) == SHA256(new_csv_file):
        return True
    else:
        return False


def SHA256(fname):
    with open(fname, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return readable_hash
