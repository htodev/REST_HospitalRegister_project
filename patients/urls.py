"""The 'urlpatterns' list route URLs to views"""

from django.urls import path
from patients import views

urlpatterns = [
    path('', views.PatientsList.as_view())
]