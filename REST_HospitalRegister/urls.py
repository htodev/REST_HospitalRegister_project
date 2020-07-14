"""REST_HospitalRegister URL Configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Smudge/', admin.site.urls),
    path('accounts/', include('project_apps.users.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('doctors/', include('project_apps.doctors.urls')),
    path('enrollment/', include('project_apps.enroll_system.urls')),
    path('patients/', include('project_apps.patients.urls'))

]
