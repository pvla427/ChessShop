from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.decorators import action, permission_classes
from . import models
from django.shortcuts import render
from rest_framework import request, viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer
from . import serializers

# Create your views here.
# def get_account(request,id):
#     user = models.UserAccount.objects.get(id = id)

# def register(request):
#     if (request.method == "POST"):
#         user = models.UserAccount()
#         user.save()
#     else:
#          pass

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

class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class CreateUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'create' and not request.user.is_authenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [CreateUser|IsAccountOwnerOrAdmin]
    queryset = User.objects.all()
    def get_queryset(self):
        return (User.objects.all() if (self.action == 'create') and not self.request.user.is_authenticated 
        else User.objects.filter(id = request.user.id))

class PublicUserDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.PublicUserSerializer
    permission_classes = [permissions.AllowAny]
    query_set = User.objects.all()