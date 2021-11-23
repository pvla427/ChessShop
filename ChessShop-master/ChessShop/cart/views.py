from django.shortcuts import render
from . import models

# Create your views here.
def order_index(request,id):
    order_items = models.OrderItem.objects.all()
    user = models.User.get_by_id(request.id)
    delivery = models.DeliveryData.objects.get(id=request.id)

def view_item(request,id):
   board = models.OrderItem.get(id = id)
   return board

def view_orders(request):
    orders = models.Order.objects.all()
    return orders

def view_delivery(request, id):
    data = models.DeliveryData.objects.get(id = id)
    return data