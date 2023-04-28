from urllib import request
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AuthenticationSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        return super().validate(attrs)
    