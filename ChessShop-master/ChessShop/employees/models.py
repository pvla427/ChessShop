from django.db import models
from django.utils.timezone import now
from django.conf import settings
import os

def get_employee_photo_upload_path(employee, filename):
    currentDateTime = now()
    relativePath = f'employees/{currentDateTime.year}{currentDateTime.month}{currentDateTime.day}{currentDateTime.hour}{currentDateTime.minute}{currentDateTime.second}{currentDateTime.microsecond}/{filename}'
    absolutePath = os.path.join(settings.MEDIA_ROOT, relativePath)
    if not os.path.exists(absolutePath):
        os.makedirs(absolutePath)
    return relativePath

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    department = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200)
    about = models.CharField(max_length=1000, null=True, blank=True)
    photo = models.ImageField(default='default_profile_picture.jpg', upload_to=get_employee_photo_upload_path)