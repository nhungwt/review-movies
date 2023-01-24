from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200, blank=True)
    infor = models.CharField(max_length=500) # contain link wiki
    publish = models.CharField(max_length=4, blank=False)
    updated = models.DateField(auto_now=True)
    img = models.CharField(max_length=500)
    des = models.CharField(max_length=200)