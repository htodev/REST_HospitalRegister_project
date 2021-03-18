"""REST_HospitalRegister URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Smudge/', admin.site.urls),
    path('accounts/', include('project_apps.users.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('enrollment/', include('project_apps.enroll_system.urls')),
    path('patients/', include('project_apps.patients.urls'))

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
