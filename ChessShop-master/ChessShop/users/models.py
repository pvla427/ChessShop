from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _

class UserAccount(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        UNKNOWN = 3, _('Not specified')
    user = OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='account')
    status = models.CharField(max_length=200)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    gender = models.SmallIntegerField(choices=Gender.choices, default=Gender.UNKNOWN)
    profilePicture = models.ImageField(default='default_profile_picture.jpg')
    lichessToken = models.CharField(max_length=1024, null=True)



# Create your models here.
