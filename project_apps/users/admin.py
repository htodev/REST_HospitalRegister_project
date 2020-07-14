"""Registers model Doctor in Django Admin interface."""


from django.contrib import admin
from project_apps.users.models import User

admin.site.register(User)
