from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/main/', views.index, name='main-index'),
    path('api/about/', views.about, name='main-about')
]