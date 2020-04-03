"""It contains authorization functionality granting
   access to Enrollment records to Doctors."""

from rest_framework.permissions import BasePermission
from doctors.models import Doctor


class IsOwner(BasePermission):
    """This class inherit BasePermission class."""

    def has_object_permission(self, request, view, obj):
        """
        Checks whether authenticated user is author of particular
        object.
        request:
        view:
        obj:
        return: True or False
        """

        try:
            doctor = Doctor.objects.get(user_id=request.user.id)
            return obj.doctor_name == doctor
        except:
            return False
