from django.db import models


class Weather(models.Model):
    Station = models.CharField(max_length=50)
    Temperature = models.IntegerField()
    Weathercol = models.CharField(max_length=25)
    windspeed = models.IntegerField()
    windgust = models.IntegerField()
    winddirection = models.CharField(max_length=10)
    humidity = models.IntegerField()
    rainfall = models.DecimalField(max_digits=9, decimal_places=3)
    pressure = models.IntegerField()
    last_update = models.DateTimeField('date published')