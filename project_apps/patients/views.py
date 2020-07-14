"""It contains all functionality related to Patient API endpoint """
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from project_apps.enroll_system.models import Enrollment


class PatientsList(APIView):
    """Base view for extract certain patient info from Enrollment records."""

    def get(self, request, *args, **kwargs):
        """
        request:
        param
        args:
        kwargs:
        return: a list with dictionaries containing data about
        all or single Patient unit.
        """

        patient_name = request.query_params.get('patient', None)
        data = Enrollment.objects.all()
        if not patient_name:
            all_patients = self._populate_response_data(data)
            return Response(all_patients, status=status.HTTP_200_OK)
        raw_patient_data = self._populate_response_data(data)
        final_patient_data = []
        for patient in raw_patient_data:
            for key, value in patient.items():
                if patient_name in value:
                    final_patient_data.append(patient)
                    break
        return Response(final_patient_data, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        """
        data: a list with dictionaries containing data about
        each Enrollment unit.
        return: a list with dictionaries containing data about patients(name and room),
        extracted from each Enrollment unit.
        """

        all_received_patients = []
        for item in data:
            temp_data = {'name': item.patient_name,
                         'room_number': item.room_number}
            all_received_patients.append(temp_data)
        return all_received_patients
