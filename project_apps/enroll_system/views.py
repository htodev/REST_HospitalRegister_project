"""It contains all functionality related to EnrollSystem API endpoints """

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from project_apps.enroll_system.models import Enrollment
from project_apps.users.models import User
from project_apps.enroll_system.serializers import EnrolmentSerializer
from project_apps.enroll_system.enrollment_permisson import IsOwner


def populate_response_data(data):
    """
    Function which process raw data.
    Args:
        data: list with dictionaries containing the from queryset

    Returns: dictionary
    """

    for item in data:
        doctor = User.objects.get(id=item['doctor_id'])
        del item['doctor_id']
        item['doctor_name'] = doctor.username
    return data


class AllEnrollments(generics.ListCreateAPIView):
    """Generic view for Create and list Enrolment records."""

    queryset = Enrollment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        """
        Overwrites built-in list method, in order to create filter functionality
        with query_params.
        Args:
            request: request
            args: args
            kwargs: kwargs

        Returns: dictionary
        """

        dr_name = request.query_params.get('doctor', None)
        if not dr_name:
            query = Enrollment.objects.all().values()
            if not query.exists():
                raise Http404
            response_data = populate_response_data(query)
            return Response(response_data, status=status.HTTP_200_OK)
        doctor = get_object_or_404(User, username=dr_name)
        enrolment_entity = Enrollment.objects.filter(doctor=doctor.id).values()
        response_data = populate_response_data(enrolment_entity)
        return Response(response_data, status=status.HTTP_200_OK)


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic view for Retrieve and Update Enrollment records."""

    queryset = Enrollment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, *args, **kwargs):
        """
        Overwrites built-in get method, in order to customise the look of output data.
        (Change User id with username)
        Args:
            request: request
            args: args
            kwargs: kwargs

        Returns: Dictionary
        """

        enrolment_entity = Enrollment.objects.filter(id=kwargs["pk"]).values()
        response_data = populate_response_data(enrolment_entity)
        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        """This method prohibit the base update method PUT and
        allows only partial update via PATCH method."""

        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
