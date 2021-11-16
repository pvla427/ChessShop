from django.db import models
from django.db.models.fields.related import ForeignKey

class Image(models.Model):
    url = models.URLField()

class Chessboard(models.Model):
    image = ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    itemName = models.CharField(max_length=1000)
    description = models.TextField()
    lengthCm = models.FloatField()
    widthCm = models.FloatField()
    heightCm = models.FloatField()
    price = models.IntegerField()
    image = models.URLField()


# Create your models here.
