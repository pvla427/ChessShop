from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('chessboards', views.ChessboardViewSet, basename='chessboard')

urlpatterns = [
    #path('', views.index, name='products-index'),
    #path('about/', views.about, name='products-about')
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 ]