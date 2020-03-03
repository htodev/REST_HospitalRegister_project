from enroll_system.models import Enrollment
from doctors.models import Doctor
from enroll_system.serializers import EnrolmentSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class AllEnrollments(generics.ListCreateAPIView):
    queryset = ''
    serializer_class = EnrolmentSerializer

    def list(self, request, *args, **kwargs):
        query = Enrollment.objects.all()
        query = query.values()
        for item in query:
            doc = Doctor.objects.get(id=item['doctor_name_id'])
            del item['doctor_name_id']
            item['doctor'] = doc.name
        return Response(query, status=status.HTTP_200_OK)

