from django.db import models

# Create your models here.

class Auto(models.Model):
    name = models.CharField(max_length= 50)
    brand = models.CharField(max_length= 30)
    year = models.CharField(max_length= 4)
    price = models.IntegerField()