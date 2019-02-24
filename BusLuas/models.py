from django.db import models
from datetime import datetime
import django.utils.timezone
# Create model for IrishRail.

class BusLuas(models.Model):
    ServerTime = models.DateTimeField(auto_now_add=True, null=True)
    TrainCode  = models.CharField(max_length=100, null=True)
    StationFullName  = models.CharField(max_length=100, null=True)
    StationCode  = models.CharField(max_length=100, null=True)
    QueryTime  = models.TimeField(null=True)
    Traindate = models.DateTimeField(auto_now_add=True, null=True)
    Origin = models.CharField(max_length=100, null=True)
    Destination = models.CharField(max_length=100, null=True)
    Origintime  = models.TimeField(null=True)
    Destinationtime = models.TimeField(null=True)
    Status = models.CharField(max_length=100, null=True)
    Lastlocation = models.CharField(max_length=100, null=True)
    Duein = models.CharField(max_length=100, null=True)
    Late = models.CharField(max_length=100, null=True)
    Exparrival =  models.TimeField(null=True)
    Expdepart =  models.TimeField(null=True)
    Scharrival =  models.TimeField(null=True)
    Schdepart =  models.TimeField(null=True)
    Direction = models.CharField(max_length=100, null=True)
    Traintype = models.CharField(max_length=100, null=True)
    Locationtype  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.TrainCode
    def __str__(self):
        return self.StationFullName
    def __str__(self):
        return self.StationCode
    def natural_key(self):
        return self.my_natural_key