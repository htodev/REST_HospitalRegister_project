from django.urls import path
from doctors import views

urlpatterns = [
    path('', views.DoctorsReview.as_view())
]