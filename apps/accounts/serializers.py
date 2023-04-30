from dataclasses import field
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from apps.accounts.signals import user_profile_signal
from apps.accounts.models import UserProfile
# from django.contrib.auth import get_user

User = get_user_model()

class AuthenticationSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        return super().validate(attrs)
    

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    user_profile = UserProfileSerializer(source="user", read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'phone_number',
            'first_name',
            'last_name',
            'password',
            'user_profile'
        ]

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)

        user.save()

        user_profile_signal.send(sender=User,
                                 instance=user,
                                 created=True,
                                 request=self.context.get("request"))

        return user
    

   

    



    