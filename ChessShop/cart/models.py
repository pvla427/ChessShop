from django.db import models
from products.models import Chessboard
from django.contrib.auth.models import User

class DeliveryMethod(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class DeliveryData(models.Model):
    deliveryMethod = models.ForeignKey(DeliveryMethod, on_delete=models.RESTRICT)
    order = models.OneToOneField('Order', on_delete=models.CASCADE, primary_key=True)
    recipientName = models.CharField(max_length=300)
    recipientPhoneNumber = models.CharField(max_length=20)
    recipientEmailAddress = models.EmailField()
    deliveryAddress = models.CharField(max_length=2000)
    postalCode = models.CharField(max_length=30)
    deliveryCost = models.IntegerField()
    arrivesWithinMin = models.DurationField()
    arrivesWithinMax = models.DurationField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderDate = models.DateTimeField()
    #isDelivery = models.BooleanField()
    #pickUpOrDeliveryLocation = models.CharField(max_length=1000)
    isActive = models.BooleanField()
    isPaid = models.BooleanField()
    comment = models.TextField()

class OrderItem(models.Model):
    item = models.ForeignKey(Chessboard, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()

# Create your models here.
