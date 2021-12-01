from django.db import models
from products.models import Chessboard
from django.contrib.auth.models import User
import datetime

class DeliveryMethod(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    costNote = models.TextField()
    deliveryCost = models.IntegerField()
    arrivesWithinMin = models.DurationField()
    arrivesWithinMax = models.DurationField()

class DeliveryData(models.Model):
    deliveryMethod = models.ForeignKey(DeliveryMethod, on_delete=models.RESTRICT)
    #курьерская служба
    order = models.OneToOneField('Order', on_delete=models.CASCADE, primary_key=True)
    recipientName = models.CharField(max_length=300)
    recipientPhoneNumber = models.CharField(max_length=20)
    recipientEmailAddress = models.EmailField()
    deliveryAddress = models.CharField(max_length=2000)

class Order(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
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

#GET:
#api/deliveryMethods - возращение списка доступных способов доставки: массив (название, приблизтельный срок доставки, вид доставки - 1 - пункт доставки, 2 - адрес; стоимость;
#свойство methods - массив, свойство puncts - массив строк с пунктами выдачи
#api/orders - 

#POST:
#order

#токен, id модели + количество, способ доставки: список  