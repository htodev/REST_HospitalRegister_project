"""Contains Doctor model."""

from django.db import models
from project_apps.users.models import User
from project_apps.doctors.enums import SpecialityEnum


class Doctor(models.Model):
    """Defines Doctor model."""

    user = models.OneToOneField(User, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=20, choices=[(s.name, s.value) for s in SpecialityEnum])

    def __str__(self):
        return f"{self.name}"

