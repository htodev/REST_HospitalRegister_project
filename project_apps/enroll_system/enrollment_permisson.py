"""It contains authorization functionality granting
   access to Enrollment records to Users."""

from rest_framework import permissions
from project_apps.users.models import User


class IsOwner(permissions.BasePermission):
    """This class inherit BasePermission class."""

    def has_object_permission(self, request, view, obj):
        """
        Checks whether authenticated user is author of particular
        object.
        Args:
            request: request
            view: view
            obj: obj
        Returns: True or False
        """

        doctor = User.objects.get(id=request.user.id)
        return obj.doctor == doctor
