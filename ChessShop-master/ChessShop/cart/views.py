from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from . import models
from . import serializers

def order_index(request,id):
    order_items = models.OrderItem.objects.all()
    user = models.User.get_by_id(request.id)
    delivery = models.DeliveryData.objects.get(id=request.id)

def view_item(request, id):
   board = models.OrderItem.get(id = id)
   return board

def view_orders(request):
    orders = models.Order.objects.all()
    return orders

def view_delivery(request, id):
    data = models.DeliveryData.objects.get(id = id)
    return data

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderItemSerializer

class DeliveryMethodSerializer(viewsets.ModelViewSet):
    queryset = models.DeliveryMethod.objects.all()
    serializer_class = serializers.DeliveryMethodSerializer

class DeliveryDataSerializer(viewsets.ModelViewSet):
    queryset = models.DeliveryData.objects.all()
    serializer_class = serializers.DeliveryDataSerializer