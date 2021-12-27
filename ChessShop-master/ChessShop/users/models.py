from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.conf import settings
import os

def get_profile_picture_upload_path(userAccount, filename):
    currentDateTime = now()
    relativePath = f'user{userAccount.user.id}/{currentDateTime.year}{currentDateTime.month}{currentDateTime.day}{currentDateTime.hour}{currentDateTime.minute}{currentDateTime.second}{currentDateTime.microsecond}/{filename}'
    absolutePath = os.path.join(settings.MEDIA_ROOT, relativePath)
    if not os.path.exists(absolutePath):
        os.makedirs(absolutePath)
    return relativePath

class UserAccount(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        UNKNOWN = 3, _('Not specified')
    user = OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='account')
    status = models.CharField(max_length=200, null=True, blank=True)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    gender = models.SmallIntegerField(choices=Gender.choices, default=Gender.UNKNOWN)
    profilePicture = models.ImageField(default='default_profile_picture.jpg', upload_to=get_profile_picture_upload_path)
    lichessToken = models.CharField(max_length=1024, null=True, blank=True)



# Create your models here.
