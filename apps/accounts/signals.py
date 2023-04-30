from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.contrib.auth import get_user_model
from apps.accounts.models import User, UserProfile


user_profile_signal = Signal()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        data = {
            'user': instance,
            'profile': kwargs.get("request").data.get("profile") #type: ignore
        }
        # print(data)
        UserProfile.objects.create(**data)

        print("User profile created...")

user_profile_signal.connect(create_user_profile)
        