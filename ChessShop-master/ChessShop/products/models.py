from django.db import models
from django.db.models.fields.related import ForeignKey

class Chessboard(models.Model):
    image = models.ImageField()
    itemName = models.CharField(max_length=1000)
    description = models.TextField()
    lengthCm = models.FloatField()
    widthCm = models.FloatField()
    heightCm = models.FloatField()
    price = models.IntegerField()


# Create your models here.
