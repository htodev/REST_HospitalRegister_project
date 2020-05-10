"""Setups URL Configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('doctors/', include('doctors.urls')),
    path('enrollment/', include('enroll_system.urls')),
    path('patients/', include('patients.urls'))

]
