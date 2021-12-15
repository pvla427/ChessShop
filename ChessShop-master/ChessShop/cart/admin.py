from django.contrib import admin
from .models import Order, OrderItem, DeliveryMethod

admin.site.register([Order, OrderItem, DeliveryMethod])

# Register your models here.
