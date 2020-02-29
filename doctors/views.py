from doctors.models import Doctor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DoctorsReview(APIView):
    def get(self, request, *args, **kwargs):
        data = Doctor.objects.all()
        response_data = self._populate_response_data(data)
        return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        name_and_specialty = []
        for doctor in data:
            temp_data = {'name': doctor.name,
                         'specialty': doctor.specialty}
            name_and_specialty.append(temp_data)
        return name_and_specialty
