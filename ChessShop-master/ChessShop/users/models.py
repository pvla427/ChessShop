from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import OneToOneField

class UserAccount(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=200)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    profilePicture = models.ImageField(default='default_profile_picture.jpg')
    city = models.CharField(max_length=100)



# Create your models here.
