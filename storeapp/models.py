from django.db import models

# Create your models here.
class Store(models.Model): 
    loc_id = models.IntegerField(default=None)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    availability_radius = models.FloatField(default=None)  
    open_hour = models.TimeField(default=None)
    close_hour = models.TimeField(default=None)
    rating = models.FloatField(default=None) 
  
    def __str__(self):  
        return str(self.id) 