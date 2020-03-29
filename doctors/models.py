from django.db import models
from users.models import User
# from django.contrib.auth.models import User
from doctors.enums import SpecialityEnum


class Doctor(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=20, choices=[(s.name, s.value) for s in SpecialityEnum])

    def __str__(self):
        return f"{self.name}"

