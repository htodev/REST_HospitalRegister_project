"""It contains serialization for Enrollment model"""

from rest_framework import serializers
from project_apps.enroll_system.models import Enrollment


class EnrolmentSerializer(serializers.ModelSerializer):
    """This class will convert Enrollment model into other format"""

    class Meta:
        """Meta class which will define how EnrolmentSerializer class
                wil behave """

        model = Enrollment
        fields = ['id', 'doctor', 'patient_name', 'symptoms', 'diagnosis', 'received_at', 'signed_out', 'room_number']

    def to_internal_value(self, data):
        try:
            data["doctor"] = self.context["request"].user.id
        except KeyError:
            raise serializers.ValidationError({"users": "User is required"})
        return super().to_internal_value(data)
