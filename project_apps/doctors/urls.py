"""The 'urlpatterns' list route URLs to views."""

from django.urls import path
from project_apps.doctors import views

urlpatterns = [
    path('create/', views.DoctorsReview.as_view()),
    path('', views.DoctorsList.as_view())
]