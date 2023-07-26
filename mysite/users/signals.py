from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Resume

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): # gets run every time a user gets created
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def create_resume(sender, instance, created, **kwargs): # gets run every time a user gets created
    if created:
        Resume.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_resume(sender, instance, **kwargs):
    instance.resume.save()

