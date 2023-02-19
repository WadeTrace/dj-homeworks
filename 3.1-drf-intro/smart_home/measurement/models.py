from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
