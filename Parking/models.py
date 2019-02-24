from django.db import models

'''
class Parking(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name
'''


class Parking(models.Model):
    id1 = models.IntegerField()
    location = models.CharField(max_length=100)
    roadname = models.CharField(max_length=100)
    noofspaces = models.IntegerField()
    spacetype = models.CharField(max_length=100)
    OBJECTID = models.IntegerField()
    Point = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=12, decimal_places=9)
    long = models.DecimalField(max_digits=12, decimal_places=9)
    last_update = models.DateTimeField('date published', null=True)