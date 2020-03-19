from enroll_system.models import Enrollment
from doctors.models import Doctor
from enroll_system.serializers import EnrolmentSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


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
            print(enrolment_entity)
            data = enrolment_entity.values
            print(data)
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
    permission_classes = [IsAuthenticated,]

    def update(self, request, *args, **kwargs):
        return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)











