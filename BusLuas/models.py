from django.db import models
from django.utils import timezone

# Create model for IrishRail.

class BusLuas(models.Model):
    ServerTime = models.DateTimeField(auto_now_add=True, null=True)
    TrainCode = models.CharField(max_length=10, null=True)
    StationFullName = models.CharField(max_length=100, null=True)
    StationCode = models.CharField(max_length=6, null=True)
    QueryTime = models.TimeField(null=True)
    TrainDate = models.DateTimeField(auto_now_add=True, null=True)
    Origin = models.CharField(max_length=100, null=True)
    Destination = models.CharField(max_length=100, null=True)
    OriginTime = models.TimeField(null=True)
    DestinationTime = models.TimeField(null=True)
    Status = models.CharField(max_length=100, null=True)
    LastLocation = models.CharField(max_length=100, null=True)
    DueIn = models.IntegerField(null=True)
    Late = models.IntegerField(null=True)
    ExpArrival = models.TimeField(null=True)
    ExpDepart = models.TimeField(null=True)
    SchArrival = models.TimeField(null=True)
    SchDepart = models.TimeField(null=True)
    Direction = models.CharField(max_length=20, null=True)
    TrainType = models.CharField(max_length=20, null=True)
    LocationType = models.CharField(max_length=1, null=True)
    cm_last_insert_dttm = models.DateTimeField(default=timezone.now, blank=True)

class IrishRailStationCode(models.Model):
    StationDesc = models.CharField(max_length=100, null=True)
    StationAlias = models.CharField(max_length=100, null=True)
    StationLatitude = models.DecimalField(max_digits=9, decimal_places=6)
    StationLongitude = models.DecimalField(max_digits=9, decimal_places=6)
    StationCode = models.CharField(max_length=6, null=True)
    StationId = models.IntegerField()
    cm_last_insert_dttm = models.DateTimeField(default=timezone.now, blank=True)