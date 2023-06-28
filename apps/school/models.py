from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Teacher, Student


class Grade(models.Model):
    name = models.CharField(
        _('Grade Name'),
        max_length=255,
    )
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.SET_NULL,
        verbose_name=_('Teacher'),
        related_name='grade_teacher',
        null=True,
        blank=True,
    )
    student = models.ManyToManyField(
        Student,
        verbose_name=_('Student'),
        related_name='grade_student',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Grade')
        verbose_name_plural = _('Grades')


class School(models.Model):
    name = models.CharField(
        _('School name'),
        max_length=255,
    )
    grade = models.ManyToManyField(
        Grade,
        verbose_name=_('Grade'),
        related_name='school',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')
