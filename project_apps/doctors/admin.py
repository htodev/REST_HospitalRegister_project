"""Registers model User in Django Admin interface."""

from django.contrib import admin
from project_apps.doctors.models import Doctor

admin.site.register(Doctor)

