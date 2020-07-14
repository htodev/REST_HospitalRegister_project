"""The 'urlpatterns' list route URLs to views"""

from django.urls import path
from project_apps.patients import views

urlpatterns = [
    path('', views.PatientsList.as_view())
]