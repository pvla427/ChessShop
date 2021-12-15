from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.serializers import Serializer
from . import models
from . import serializers

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class ChessboardViewSet(viewsets.ModelViewSet):
    queryset = models.Chessboard.objects.all()
    permission_classes = [permissions.IsAdminUser|ReadOnly]
    serializer_class = serializers.ChessboardSerializer
