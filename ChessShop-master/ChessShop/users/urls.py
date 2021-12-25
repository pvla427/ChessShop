from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='user')
router.register('users/public', views.PublicUserDataViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
     #path('', views.index, name='main-index'),
     #path('about/', views.about, name='main-about')
 ]