from rest_framework import serializers
from enroll_system.models import Enrollment


class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
