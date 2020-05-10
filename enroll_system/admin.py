"""Registers model User in Django Admin interface."""

from django.contrib import admin
from enroll_system.models import Enrollment

admin.site.register(Enrollment)
