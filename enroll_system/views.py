"""It contains all functionality related to EnrollSystem API endpoints """

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from enroll_system.models import Enrollment
from doctors.models import Doctor
from enroll_system.serializers import EnrolmentSerializer
from enroll_system.enrollment_permisson import IsOwner


class AllEnrollments(generics.ListCreateAPIView):
    """Generic view for Create single Enrolment record."""

    queryset = Enrollment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        """
        request:
        args:
        kwargs:
        return: [
                    {
                    "id": "",
                    "patient_name": "",
                    "symptoms": "",
                    "diagnosis": "",
                    "received_at": "",
                    "signed_out": "",
                    "room_number": "",
                    "doctor": ""
                    }
                ]
        """

        dr_name = request.query_params.get('doctor', None)
        if not dr_name:
            query = Enrollment.objects.all()
            if not query.exists():
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            query = query.values()
            response_data = self._populate_response_data(query)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            doctor = get_object_or_404(Doctor, name=dr_name)
            enrolment_entity = Enrollment.objects.filter(doctor_name=doctor)
            data = enrolment_entity.values()
            response_data = self._populate_response_data(data)
            return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        """
        data: [
                    {
                    "id": "",
                    "doctor_name_id": "",
                    "patient_name": "",
                    "symptoms": "",
                    "diagnosis": "",
                    "received_at": "",
                    "signed_out": "",
                    "room_number": "",
                    }
                ]
        return: [
                    {
                    "id": "",
                    "patient_name": "",
                    "symptoms": "",
                    "diagnosis": "",
                    "received_at": "",
                    "signed_out": "",
                    "room_number": "",
                    "doctor": ""
                    }
                ]
        """

        for item in data:
            dr = Doctor.objects.get(id=item['doctor_name_id'])
            del item['doctor_name_id']
            item['doctor'] = dr.name
        return data


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic view for Retrieve and Update Enrollment records."""

    queryset = Enrollment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        """This method prohibit the base update method PUT and
        allows only partial update via PATCH method."""

        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


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
