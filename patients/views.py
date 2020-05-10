"""It contains all functionality related to Patient API endpoint """
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from enroll_system.models import Enrollment


class PatientsList(APIView):
    """Base view for extract certain patient info from Enrollment records."""

    def get(self, request, *args, **kwargs):
        """
        request:
        param
        args:
        kwargs:
        return: [
                    {
                        "name": "",
                        "room_number": ""
                    }
                ]
        """

        patient_name = request.query_params.get('patient', None)
        data = Enrollment.objects.all()
        if not patient_name:
            all_patients = self._populate_response_data(data)
            return Response(all_patients, status=status.HTTP_200_OK)
        else:
            all_patients = self._populate_response_data(data)
            all_patients = all_patients
            single_patient = []
            for patient in all_patients:
                for key, value in patient.items():
                    if patient_name in value:
                        single_patient.append(patient)
                        break
            return Response(single_patient, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        """
        data: dict of all Enrollment records
        return:[{'name: patient, 'room_number': number}]
        """

        all_received_patients = []
        for item in data:
            temp_data = {'name': item.patient_name,
                         'room_number': item.room_number}
            all_received_patients.append(temp_data)
        return all_received_patients