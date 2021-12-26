from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now

def get_chessboard_image_upload_path(chessboard, filename):
    current_date_time = now()
    return f'chessboard{chessboard.id}/{current_date_time.year}{current_date_time.month}{current_date_time.day}{current_date_time.hour}{current_date_time.minute}{current_date_time.second}{current_date_time.microsecond}/{filename}'

class Chessboard(models.Model):
    itemName = models.CharField(max_length=1000)
    description = models.TextField()
    lengthCm = models.FloatField()
    widthCm = models.FloatField()
    heightCm = models.FloatField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=get_chessboard_image_upload_path, default='default_board_image.png')


# Create your models here.
