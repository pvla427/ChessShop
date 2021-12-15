from django.db.models import fields
from rest_framework import serializers

from . import models

class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryMethod
        fields = ['name', 'description', 'costNote', 'deliveryCost', 'arrivesWithinMin', 'arrivesWithinMax']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['item', 'count']

class OrderSerializer(serializers.ModelSerializer):
    orderItems = OrderItemSerializer(many=True)
    class Meta:
        model = models.Order
        fields = ['orderDate', 'isActive', 'isPaid', 'comment', 
        'recipientName', 'recipientPhoneNumber', 'recipientEmailAddress', 
        'deliveryAddress', 'deliveryMethod', 'orderItems']
    def create(self, validated_data):
        orderItemsData = validated_data.pop('orderItems')
        order = models.Order.objects.create(user=self.context['request'].user, **validated_data)
        for orderItemData in orderItemsData:
            models.OrderItem.objects.create(order=order, **orderItemData)
        return order
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if 'orderItems' not in validated_data:
            return instance
        orderItemsData = validated_data['orderItems']
        for orderItemData in orderItemsData:
            orderItem, created = instance.orderItem_set.get_or_create(
                item=orderItemData['item'], 
                defaults={'item': orderItemData['item'], 'order': instance})
            orderItem.count = orderItemData['count']
            orderItem.save()
        return instance