from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now

def get_chessboard_image_upload_path(chessboardOption, filename):
    current_date_time = now()
    return f'chessboard{chessboardOption.chessboard.id}/{chessboardOption.name}/{current_date_time.year}{current_date_time.month}{current_date_time.day}{current_date_time.hour}{current_date_time.minute}{current_date_time.second}{current_date_time.microsecond}/{filename}'

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
