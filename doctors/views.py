"""It contains all functionality related to Doctors API endpoints."""

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer


class DoctorsReview(generics.CreateAPIView):
    """Generic view for Create doctors."""

    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated,]


class DoctorsList(APIView):
    """A base view which lists all doctors."""

    def get(self, request, *args, **kwargs):
        """
        Get doctors list
        request:
        param args:
        param kwargs:
        return: dict with processed doctor's info
        """

        data = Doctor.objects.all()
        response_data = self._populate_response_data(data)
        return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        """
        data: dict with all info about every doctor
        return: [{doctor_name: <name>, speciality: <specialty>}}
        """

        name_and_specialty = []
        for doctor in data:
            temp_data = {'name': doctor.name,
                         'specialty': doctor.specialty}
            name_and_specialty.append(temp_data)
        return name_and_specialty
