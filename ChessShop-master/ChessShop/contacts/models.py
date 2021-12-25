from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)

class ContactEntry(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=500)


# Create your models here.
