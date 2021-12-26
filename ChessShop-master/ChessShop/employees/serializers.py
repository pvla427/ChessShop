from django.db.models import fields
from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'firstName', 'lastName', 'patronymic', 'department', 'position', 'about', 'photo']