from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class GenderChoices(TextChoices):
    MALE = "Мale", _("Male")
    FEMALE = "Female", _("Female")
