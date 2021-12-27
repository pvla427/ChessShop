from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now
from django.conf import settings
import os

def get_chessboard_image_upload_path(chessboardOption, filename):
    currentDateTime = now()
    relativePath = f'chessboard{chessboardOption.chessboard.id}/{chessboardOption.name}/{currentDateTime.year}{currentDateTime.month}{currentDateTime.day}{currentDateTime.hour}{currentDateTime.minute}{currentDateTime.second}{currentDateTime.microsecond}/{filename}'
    absolutePath = os.path.join(settings.MEDIA_ROOT, relativePath)
    if not os.path.exists(absolutePath):
        os.makedirs(absolutePath)
    return relativePath

class Chessboard(models.Model):
    itemName = models.CharField(max_length=1000, default='Доска')
    description = models.TextField(default='описание')
    lengthCm = models.FloatField(default=10.0)
    widthCm = models.FloatField(default=10.0)
    heightCm = models.FloatField(default=10.0)
    price = models.IntegerField(default=5000)
    weightKg = models.FloatField(default=1.0)
    powerW = models.FloatField(default=30.0)
    driveType = models.CharField(max_length=100, default='шаговый')

class ChessboardOption(models.Model):
    chessboard = models.ForeignKey(Chessboard, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=100, default='вариация')
    image = models.ImageField(upload_to=get_chessboard_image_upload_path, default='default_board_image.png')


# Create your models here.
