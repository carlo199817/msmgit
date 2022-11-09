from django.db import models
from django.utils import timezone
from authentication.models import User
from django.urls import reverse
from PIL import Image
from notifications.signals import notify
from django.utils.text import Truncator

# models from my understanding are the location of all the info about your data. you use it to make databases


class Store(models.Model):
    store= models.CharField(max_length=200, blank=True)
    timenow = models.CharField(max_length=200, blank=True)
    datenow = models.CharField(max_length=200, blank=True)    # caption is a field in this Post model. it specifies a class attribute Charfield and represents a database column. blank=True lets the field be optional left empty
    date_posted = models.DateTimeField(default=timezone.now)  # instead of hard setting the time this timezone.now takes the users timezone into consideration.
    date_updated = models.DateTimeField('date_updated', auto_now=True)
    author = models.ForeignKey(User, related_name='store', on_delete=models.CASCADE)  # foreign key calls on an outside model whether imported or in this file, CASCADE will delete the post if
    latitude = models.CharField(max_length=200, blank=True)
    longitude = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="post_images/%Y/%m/%d/", null=True, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.store

class SProduct(models.Model):
    sproduct = models.ForeignKey(Store, related_name='sproduct', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    quantity = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.sproduct)+"  "+self.name+" "+self.quantity+" "+self.price

class SPosm(models.Model):
    sposm = models.ForeignKey(Store, related_name='sposm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    quantity = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.sposm)+"  "+self.name+" "+self.quantity+" "+self.price