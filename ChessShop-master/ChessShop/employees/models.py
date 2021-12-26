from django.db import models
from django.utils.timezone import now

def get_employee_photo_upload_path(employee, filename):
    current_date_time = now()
    return f'user{employee.id}/{current_date_time.year}{current_date_time.month}{current_date_time.day}{current_date_time.hour}{current_date_time.minute}{current_date_time.second}{current_date_time.microsecond}/{filename}'

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    about = models.CharField(max_length=1000)
    photo = models.ImageField(default='default_profile_picture.jpg', upload_to=get_employee_photo_upload_path)
