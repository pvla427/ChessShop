from django.db import models
from products.models import Chessboard
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

class DeliveryMethod(models.Model):
    class DeliveryType(models.IntegerChoices):
        PICKUP = 1, _('Pickup location')
        ADDRESS = 2, _('Address')
    name = models.CharField(max_length=200)
    description = models.TextField()
    costNote = models.TextField()
    deliveryCost = models.IntegerField()
    arrivesWithinMin = models.DurationField()
    arrivesWithinMax = models.DurationField()
    deliveryType = models.SmallIntegerField(choices=DeliveryType.choices, default=DeliveryType.PICKUP)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    deliveryMethod = models.ForeignKey(DeliveryMethod, on_delete=models.RESTRICT)
    orderDate = models.DateTimeField(default=now)
    isActive = models.BooleanField()
    isPaid = models.BooleanField()
    comment = models.TextField()
    deliveryCompany = models.CharField(max_length=200)
    recipientName = models.CharField(max_length=300)
    recipientPhoneNumber = models.CharField(max_length=20)
    recipientEmailAddress = models.EmailField()
    deliveryAddress = models.CharField(max_length=2000)

class OrderItem(models.Model):
    item = models.ForeignKey(Chessboard, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderItems')
    count = models.IntegerField()