import csv;
import hashlib
import urllib.request
from WeatherPollution import views



def csv_update_validate(old_csv_file,new_csv_file):
    views.pull_weather_csv(new_csv_file)
    if SHA256(old_csv_file) == SHA256(new_csv_file):
        print("matched")
        return True
    else:
        print("not matched")
        return False


def SHA256(fname):
    with open(fname, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return(readable_hash)