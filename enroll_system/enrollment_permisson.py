from rest_framework.permissions import BasePermission
from doctors.models import Doctor


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            doctor = Doctor.objects.get(user_id=request.user.id)
            return obj.doctor_name == doctor
        except:
            return False
