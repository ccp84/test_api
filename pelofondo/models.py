from django.db import models


# Create your models here.
class Ride(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stacktime = models.DateTimeField(null=True)
    stackleader = models.CharField(max_length=100, null=True)
