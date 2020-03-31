"""It contains serialization for Enrollment model"""

from rest_framework import serializers
from enroll_system.models import Enrollment


class EnrolmentSerializer(serializers.ModelSerializer):
    """This class will convert Enrollment model into other format"""

    class Meta:
        """Meta class which will define how EnrolmentSerializer class
                wil behave """

        model = Enrollment
        fields = '__all__'
