from django.db import models

'''
class Bike(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name
'''

class Bike(models.Model):
    number = models.IntegerField()
    contract_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    position_lat = models.DecimalField(max_digits=9, decimal_places=6)
    position_lng = models.DecimalField(max_digits=9, decimal_places=6)
    banking = models.BooleanField(max_length=100)
    bonus = models.CharField(max_length=100)
    bike_stands = models.CharField(max_length=100)
    available_bike_stands = models.CharField(max_length=100)
    available_bikes = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    last_update = models.DateTimeField('date published')
