"""Contains Enrollment model"""

from django.db import models
from project_apps.users.models import User


class Enrollment(models.Model):
    """Defines Enrollment model"""

    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=80)
    diagnosis = models.CharField(max_length=30)
    received_at = models.DateTimeField(auto_now=True)
    signed_out = models.BooleanField(default=False)
    room_number = models.CharField(max_length=5)


