"""Contains User model and UserManger."""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings


class CustomUserManager(UserManager):
    """
    Customise UserManager behaviour.
    """
    use_in_migrations = True

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Method which relates super user and customise it.
        Args:
            email: email
            password: password
            **extra_fields: extra_fields

        Returns: User

        """
        user = super().create_superuser(
            email=email,
            **extra_fields
        )
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Defines custom user model
    """

    username = models.CharField(unique=True, max_length=50, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    specialty = models.CharField(choices=settings.SPECIALITY, blank=True, max_length=50)
    image = models.ImageField(upload_to='users', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
