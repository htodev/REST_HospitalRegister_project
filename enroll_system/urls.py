from django.urls import path
from enroll_system import views
urlpatterns = [
    path('', views.AllEnrollments.as_view()),
    path('<int:pk>', views.EnrollmentDetail.as_view()),
    path('patients/', views.PatientsList.as_view())
]
