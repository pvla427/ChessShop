from django.db.models import fields
from rest_framework import serializers

from . import models

class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryMethod
        fields = ['name', 'description', 'costNote', 'deliveryCost', 'arrivesWithinMin', 'arrivesWithinMax']

class DeliveryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryData
        fields = ['order', 'recipientName', 'recipientPhoneNumber', 'recipientEmailAddress', 'deliveryAddress', 'deliveryMethod']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['item', 'order', 'count']

class OrderSerializer(serializers.ModelSerializer):
    deliveryData = DeliveryMethodSerializer()
    orderItems = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    class Meta:
        model = models.Order
        fields = ['user', 'orderDate', 'isActive', 'isPaid', 'comment', 'orderItems']