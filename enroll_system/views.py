from enroll_system.models import Enrollment
from doctors.models import Doctor
from enroll_system.serializers import EnrolmentSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from enroll_system.enrollment_permisson import IsOwner


class AllEnrollments(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        dr_name = request.query_params.get('doctor', None)
        if not dr_name:
            query = Enrollment.objects.all()
            query = query.values()
            response_data = self._populate_response_data(query)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            doctor = Doctor.objects.get(name=dr_name)
            enrolment_entity = Enrollment.objects.get(doctor_name=doctor)
            data = enrolment_entity.values
            response_data = self._populate_response_data(data)
            return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        for item in data:
            dr = Doctor.objects.get(id=item['doctor_name_id'])
            del item['doctor_name_id']
            item['doctor'] = dr.name
        return data


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class PatientsList(APIView):

    def get(self, request, *args, **kwargs):
        patient_name = request.query_params.get('patient', None )
        print((patient_name))
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
        all_received_patients = []
        for item in data:
            temp_data = {'name': item.patient_name,
                         'room_number': item.room_number}
            all_received_patients.append(temp_data)
        return all_received_patients
