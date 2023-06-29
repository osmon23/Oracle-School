from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from config import settings
from .models import Student


@receiver(post_save, sender=Student)
def send_student_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'Notification of the creation of a student'
        message = f'{instance.full_name} student successfully created.'
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email
        send_mail(subject, message, from_email, [to_email])
