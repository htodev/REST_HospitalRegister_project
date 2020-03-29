"""
Registers model User in Django Admin interface
"""

from django.contrib import admin
from users.models import User

admin.site.register(User)
