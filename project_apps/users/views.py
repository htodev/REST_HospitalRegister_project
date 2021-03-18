"""It contains all functionality related to User API endpoints """

from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MyTokenObtainPairSerializer, UserDetailSerializer, ListUsersSerializer
from .models import User


class MyTokenObtainPairView(TokenObtainPairView):  # pylint: disable=abstract-method
    """This class takes the customised serializer in order to
    return user email."""

    serializer_class = MyTokenObtainPairSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get_object(self):
        """
        This method allows us to get User model
        without need of PK.

        Returns:

        """

        return get_object_or_404(User, id=self.request.user.id)


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer
