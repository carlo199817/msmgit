from django.db import models
from django.utils import timezone
from authentication.models import User
from django.urls import reverse
from PIL import Image
from notifications.signals import notify
from django.utils.text import Truncator

# models from my understanding are the location of all the info about your data. you use it to make databases


class ProductInventory(models.Model):
    product_no = models.CharField(max_length=200, blank=True)
    sku = models.CharField(max_length=200, blank=True)
    product = models.CharField(max_length=200, blank=True)
    quantity = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    datenow = models.CharField(max_length=200, blank=True)    # caption is a field in this Post model. it specifies a class attribute Charfield and represents a database column. blank=True lets the field be optional left empty
    date_posted = models.DateTimeField(default=timezone.now)  # instead of hard setting the time this timezone.now takes the users timezone into consideration.
    date_updated = models.DateTimeField('date_updated', auto_now=True)
    author = models.ForeignKey(User, related_name='inventory', on_delete=models.CASCADE)  # foreign key calls on an outside model whether imported or in this file, CASCADE will delete the post if
    def __str__(self):
        return self.product+"   "+self.quantity +" "+self.price

class PosmInventory(models.Model):
    posm_no = models.CharField(max_length=200, blank=True)
    sku = models.CharField(max_length=200, blank=True)
    posm = models.CharField(max_length=200, blank=True)
    quantity = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    datenow = models.CharField(max_length=200, blank=True)    # caption is a field in this Post model. it specifies a class attribute Charfield and represents a database column. blank=True lets the field be optional left empty
    date_posted = models.DateTimeField(default=timezone.now)  # instead of hard setting the time this timezone.now takes the users timezone into consideration.
    date_updated = models.DateTimeField('date_updated', auto_now=True)
    author = models.ForeignKey(User, related_name='inventory2', on_delete=models.CASCADE)  # foreign key calls on an outside model whether imported or in this file, CASCADE will delete the post if
    def __str__(self):
        return self.posm+"   "+self.quantity +" "+self.price
