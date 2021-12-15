from django.db.models import fields
from rest_framework import serializers

from . import models

class ChessboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chessboard
        fields = ['id', 'itemName', 'description', 'lengthCm', 'widthCm', 'heightCm', 'price', 'image']