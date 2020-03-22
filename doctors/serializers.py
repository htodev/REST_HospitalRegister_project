from rest_framework import serializers
from doctors.models import Doctor


class DoctorSeializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
