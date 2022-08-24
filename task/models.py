from django.db import models

# Create your models here.


class FlightInfo(models.Model):
    airline = models.CharField(max_length=10, null=False, blank=False)
    flight_number = models.CharField(max_length=10, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    info = models.JSONField(blank=False, null=False)
