from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .constants import GenderChoices


class Teacher(AbstractUser):
    phone_number = PhoneNumberField(
        _('Phone Number'),
        unique=True,
        max_length=13,
    )
    grade = models.CharField(
        _('Grade'),
        max_length=255,
        null=True,
        blank=True,
    )
    subject = models.CharField(
        _('Subject'),
        max_length=255,
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}: {self.phone_number}'

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ('-id',)


class Student(models.Model):
    full_name = models.CharField(
        _('Full Name'),
        max_length=255,
    )
    email = models.EmailField(
        _('Email'),
        unique=True,
        max_length=255,
    )
    date_of_birth = models.DateField(
        _('Date of birth'),
        default=None,
    )
    grade = models.CharField(
        _('Grade'),
        max_length=255,
        null=True,
        blank=True,
    )
    address = models.CharField(
        _('Address'),
        max_length=255,
    )
    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to='students',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
