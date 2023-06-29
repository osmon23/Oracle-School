from django.core.mail import send_mail
from django.conf import settings

from .models import Student


def send_newsletter(subject, message):
    students = Student.objects.all()
    recipient_list = [student.email for student in students]
    for recipient_email in recipient_list:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])
