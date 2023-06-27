from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class GenderChoices(TextChoices):
    MALE = "М", _("Мужской")
    FEMALE = "Ж", _("Женский")
