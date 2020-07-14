"""It contains all functionality related to EnrollSystem API endpoints """

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from project_apps.enroll_system.models import Enrollment
from project_apps.doctors.models import Doctor
from project_apps.enroll_system.serializers import EnrolmentSerializer
from project_apps.enroll_system.enrollment_permisson import IsOwner


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
        return: a list with dictionaries containing data about
        each Enrollment unit.
        """

        dr_name = request.query_params.get('doctor', None)
        if not dr_name:
            query = Enrollment.objects.all()
            if not query.exists():
                raise Http404
            query = query.values()
            response_data = self._populate_response_data(query)
            return Response(response_data, status=status.HTTP_200_OK)
        doctor = get_object_or_404(Doctor, name=dr_name)
        enrolment_entity = Enrollment.objects.filter(doctor_name=doctor)
        data = enrolment_entity.values()
        response_data = self._populate_response_data(data)
        return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def _populate_response_data(data):
        """
        data: list with dictionaries containing the raw data from
        the queryset.
        return: data with replaced keys 'doctor_id_id'  with 'doctor_name'.
        """

        for item in data:
            dr = Doctor.objects.get(id=item['doctor_name_id'])
            del item['doctor_name_id']
            item['doctor_name'] = dr.name
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
