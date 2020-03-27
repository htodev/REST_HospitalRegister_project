from django.urls import path
from doctors import views

urlpatterns = [
    path('creation/', views.DoctorsReview.as_view()),
    path('', views.DoctorsList.as_view())
]