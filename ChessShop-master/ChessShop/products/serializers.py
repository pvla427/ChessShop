from django.db.models import fields
from rest_framework import serializers

from . import models

class ChessboardOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChessboardOption
        fields = ['name', 'image']

class ChessboardSerializer(serializers.ModelSerializer):
    options = ChessboardOptionSerializer()
    class Meta:
        model = models.Chessboard
        fields = ['id', 'itemName', 'description', 'lengthCm', 'widthCm', 'heightCm', 
        'price', 'weightKg', 'powerW', 'driveType', 'options']
    def create(self, validated_data):
        chessboardOptionsData = validated_data.pop('options')
        newChessboard = models.Chessboard.objects.create(**validated_data)
        for chessboardOptionData in chessboardOptionsData:
            models.ChessboardOption.objects.create(chessboard=newChessboard, **chessboardOptionData)
        return newChessboard
    # def update(self, instance, validated_data):
    #     if 'options' in validated_data:
    #         chessboardOptionsData = validated_data.pop('options')
    #         for chessboardOptionData in chessboardOptionsData:
    #             chessboardOption, created = instance.options.get_or_create(
    #                 name=chessboardOptionData['name']
    #             )
    #     return super().update(instance, validated_data)