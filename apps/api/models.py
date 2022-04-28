from django.db import models

# Create your models here.
class Company(models.Model):
    nombre = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    found = models.DateField()
    city = models.CharField(max_length=100)
    