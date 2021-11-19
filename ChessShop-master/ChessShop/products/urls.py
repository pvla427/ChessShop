from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products-index'),
     path('about/', views.about, name='products-about')
 ]