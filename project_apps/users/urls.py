"""User url configuration."""

from django.urls import path
from django.views.defaults import page_not_found
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView, UserDetail, UsersList

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserDetail.as_view(), name='profile'),
    path('all/', UsersList.as_view(), name='profiles'),
    path('verify-email/', page_not_found, {'exception': Exception()}, name='verify-email'),
    path('register-email/', page_not_found, {'exception': Exception()}, name='register-email'),
]
