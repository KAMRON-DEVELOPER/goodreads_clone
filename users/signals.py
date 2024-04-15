
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from django.core.mail import send_mail


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        if instance.email:
            send_mail(
                subject='Welcome home!',
                message=f"Hi user {instance.username}!",
                from_email='atajanovkamronbek2003@gmail.com',
                recipient_list=[instance.email],
            )
