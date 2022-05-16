from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import ADC

from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=ADC)
# def createProfile(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         alteon = ADC.objects.create(
#             user=user,
#             username=user.username,
#             email=user.email,
#             name=user.first_name,
#         )

# subject = 'Welcome to DevSearch'
# message = 'We are glad you are here!'
#
# send_mail(
#     subject,
#     message,
#     settings.EMAIL_HOST_USER,
#     [profile.email],
#     fail_silently=False,
# )

def updateAlteon(sender, instance, created, **kwargs):
    ADC = instance
    alteon = ADC.MAC

    if created == False:
        alteon.Management = alteon.Management
        alteon.Platform = alteon.Platform
        # user.email = profile.email
        alteon.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


# post_save.connect(createProfile, sender=User)
post_save.connect(updateAlteon, sender=ADC)
post_delete.connect(deleteUser, sender=ADC)
