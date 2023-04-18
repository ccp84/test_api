from django.db import models


# Create your models here.
class Ride(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    length = models.IntegerField()
    datetime = models.DateTimeField()
    stacktime = models.DateTimeField()
    stackleader = models.CharField(max_length=100)
