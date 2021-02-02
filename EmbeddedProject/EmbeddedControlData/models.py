from django.db import models


# Create your models here.
class WorkingData(models.Model):
    turn_off_led_if_light = models.IntegerField(default=1)
    light_start_hour = models.IntegerField(default=6)
    light_end_hour = models.IntegerField(default=19)
    ambient_temp = models.IntegerField(default=30)
    ambient_humidity = models.IntegerField(default=50)
    soil_humidity = models.IntegerField(default=50)