from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Teacher, Student


class Classroom(models.Model):
    name = models.CharField(
        _('Classroom name'),
        max_length=255,
    )
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name=_('Teacher'),
        related_name='classroom_teacher',
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name=_('Student'),
        related_name='classroom_student',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classrooms')


class School(models.Model):
    name = models.CharField(
        _('School name'),
        max_length=255,
    )
    classrooms = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        verbose_name=_('Classrooms'),
        related_name='school',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')
