from django.db import models


class Weather(models.Model):
    Station = models.CharField(max_length=50 ,null=True)
    Temperature = models.IntegerField(null=True)
    Weathercol = models.CharField(max_length=25 ,null=True)
    windspeed = models.IntegerField(null=True)
    windgust = models.IntegerField(null=True)
    winddirection = models.CharField(max_length=10,null=True)
    humidity = models.IntegerField()
    rainfall = models.DecimalField(max_digits=9, decimal_places=3,null=True)
    pressure = models.IntegerField(null=True)
    last_update = models.DateTimeField('date published',null=True)