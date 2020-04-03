"""It blocks needless built-in urls from  REST Register Module."""

from django.urls import path
from django.views.defaults import page_not_found

urlpatterns = [
    path('verify-email/', page_not_found, {'exception': Exception()}, name='verify-email'),
    path('register-email/', page_not_found, {'exception': Exception()}, name='register-email'),
    path('profile/', page_not_found, {'exception': Exception()}, name='profile')
]