from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), # Receive username and password.
    path('register/', RegisterView.as_view(), name='register'), # Receive data for creation of new user.
    path('token/check/', TokenVerifyView.as_view(), name='check-token'), # Receive token
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'), # Receive refresh token
]
