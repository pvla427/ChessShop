from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
 ]