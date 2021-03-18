"""Serializers for User functionality."""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):  # pylint: disable=abstract-method
    """This class encrypts user email in the tokens."""

    def get_token(self, user):
        """
        This method apply actual encryption of User email.

        Args:
            user:

        Returns: access and refresh tokens

        """

        token = super().get_token(user)
        token['email'] = user.email
        return token


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'specialty', 'image']
        read_only_fields = ['email']


class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'specialty', 'image']
        read_only_fields = ['username', 'specialty', 'image']
