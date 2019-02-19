from django.db import models


class Weather(models.Model):
    Station = models.CharField(max_length=100)
    Temperature = models.IntegerField()
    Weathercol = models.CharField(max_length=25)
    windspeed = models.CharField(max_length=5)
    windgust = models.CharField(max_length=5)
    winddirection = models.CharField(max_length=10)
    humidity = models.IntegerField()
    rainfall = models.DecimalField(max_digits=9, decimal_places=6)
    pressure = models.CharField(max_length=5)