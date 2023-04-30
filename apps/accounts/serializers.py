from dataclasses import fields
from urllib import request
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        return super().validate(attrs)
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"