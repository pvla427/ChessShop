from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

def get_profile_picture_upload_path(userAccount, filename):
    current_date_time = now()
    return f'user{userAccount.user.id}/{current_date_time.year}{current_date_time.month}{current_date_time.day}{current_date_time.hour}{current_date_time.minute}{current_date_time.second}{current_date_time.microsecond}/{filename}'

class UserAccount(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        UNKNOWN = 3, _('Not specified')
    user = OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='account')
    status = models.CharField(max_length=200, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    patronymic = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    gender = models.SmallIntegerField(choices=Gender.choices, default=Gender.UNKNOWN)
    profilePicture = models.ImageField(default='default_profile_picture.jpg', upload_to=get_profile_picture_upload_path)
    lichessToken = models.CharField(max_length=1024, null=True)



# Create your models here.
