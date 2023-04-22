from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver

from .models import Profile 

@receiver(signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
