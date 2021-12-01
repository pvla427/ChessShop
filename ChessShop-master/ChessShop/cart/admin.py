from django.contrib import admin
from .models import Order, OrderItem, DeliveryData, DeliveryMethod

admin.site.register([Order, OrderItem, DeliveryData, DeliveryMethod])

# Register your models here.
