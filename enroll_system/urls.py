from django.urls import path
from enroll_system import views
urlpatterns = [
    path('', views.AllEnrollments.as_view())
]
