from django.shortcuts import render
from . import models
from products.models import Chessboard
# Create your views here.
def order_index(request,id):
    order_items = models.OrderItem.objects.get_all()
    user = models.User.get_by_id(request.id)
    delivery = models.DeliveryData.objects.get(id=request.id)

def view_item(request,id):
    board = models.Chessboard.objects.get(id=request.id)