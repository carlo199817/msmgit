
from django.db import models




class Task(models.Model):
    email = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.email

class Gps(models.Model):
    gps = models.ForeignKey(Task, related_name='gps', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=200, blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.latitude)+" "+str(self.longitude)
