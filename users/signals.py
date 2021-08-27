# Created to link user to profile once a user is created

from django.db.models.signals import post_save # When user is saved a signal will be created
from django.contrib.auth.models import User # Sender of the signal
from django.dispatch import receiver # Receiver of signal - a function that performs some task
from .models import Profile

@receiver(post_save, sender = User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

# Explanation: if user is created then saved, run the function and created a profile as well

@receiver(post_save, sender = User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Explanation: after profile is created above, profile is saved