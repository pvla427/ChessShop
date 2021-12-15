from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.serializers import Serializer
from . import models
from . import serializers

# def order_index(request,id):
#     order_items = models.OrderItem.objects.all()
#     user = models.User.get_by_id(request.id)
#     delivery = models.DeliveryData.objects.get(id=request.id)

# def view_item(request, id):
#    board = models.OrderItem.get(id = id)
#    return board

# def view_orders(request):
#     orders = models.Order.objects.all()
#     return orders

# def view_delivery(request, id):
#     data = models.DeliveryData.objects.get(id = id)
#     return data

class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsUserOrAdmin]
    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user)

class DeliveryMethodSerializer(viewsets.ModelViewSet):
    queryset = models.DeliveryMethod.objects.all()
    serializer_class = serializers.DeliveryMethodSerializer
    permissions_classes = [permissions.IsAdminUser|ReadOnly]