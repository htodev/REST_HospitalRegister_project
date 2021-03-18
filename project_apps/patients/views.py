"""It contains all functionality related to Patient API endpoint. """

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from project_apps.enroll_system.models import Enrollment


class PatientsList(APIView):
    """Base view for extract certain patient info from Enrollment records."""

    def get(self, request, *args, **kwargs):
        """
        Get method which takes all Enrollment object form DB, extract needed data
        process it and turns it as dictionary.
        Args:
            request: request
            *args: args
            **kwargs: kwargs

        Returns: Dictionary
        """

        patient_name = request.query_params.get('patient', None)
        data = Enrollment.objects.all()
        if not patient_name:
            all_patients = self._populate_response_data(data)
            return Response(all_patients, status=status.HTTP_200_OK)
        patient = get_object_or_404(Enrollment, patient_name=patient_name)
        return Response({"patient_name": patient.patient_name, "room": patient.room_number}, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        """
        It Processes the passed data, and turns it back in needed format.

        Args:
            data: list with dictionaries

        Returns: list with dictionaries
        """

        all_received_patients = []
        for item in data:
            temp_data = {'name': item.patient_name,
                         'room_number': item.room_number}
            all_received_patients.append(temp_data)
        return all_received_patients
