"""The 'urlpatterns' list route URLs to views"""

from django.urls import path
from project_apps.enroll_system import views
urlpatterns = [
    path('', views.AllEnrollments.as_view()),
    path('<int:pk>/', views.EnrollmentDetail.as_view()),
]
