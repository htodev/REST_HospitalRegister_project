"""Registers User model in Django Admin interface."""

from django.contrib import admin
from project_apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configure User in Admin interface"""
    readonly_fields = ["password"]
    fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_display = ('username', 'email',)
    search_fields = ('username', 'email')
