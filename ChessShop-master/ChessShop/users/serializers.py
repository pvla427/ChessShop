from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccount
        fields = ['status', 'firstName', 'lastName', 
        'patronymic', 'city', 'experience', 'gender', 'profilePicture', 'lichessToken']

class UserSerializer(serializers.ModelSerializer):
    account = UserAccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff', 'is_active', 'account']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'is_staff': {'read_only': True}
        }
    def create(self, validated_data):
        accountData = validated_data.pop('account')
        user = User.objects.create(**validated_data)
        models.UserAccount.create(user=user, **accountData)
        return user
    def update(self, instance, validated_data):
        if ('password' in validated_data):
            password = validated_data.pop('password')
            instance.set_password(password)
        if ('account' in validated_data):
            #account = instance.account
            accountData = validated_data.pop('account')
            models.UserAccount.objects.filter(user=instance).update(**accountData)

        return super().update(instance, validated_data)

class PublicUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        models.UserAccount
        fields = ['status', 'firstName', 'lastName', 
        'patronymic', 'city', 'experience', 'gender', 'profilePicture']

class PublicUserSerializer(serializers.ModelSerializer):
    account = PublicUserAccountSerializer()
    class Meta:
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'account']