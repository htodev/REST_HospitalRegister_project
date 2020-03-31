"""It contains serialization for Doctor model."""
from rest_framework import serializers
from doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """This class will convert Doctor model into other format."""

    class Meta:
        """Meta class which will define how DoctorSerializer class
         wil behave."""

        model = Doctor
        fields = '__all__'
