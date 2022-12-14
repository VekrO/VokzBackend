from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), # Receive username and password.
    path('token/check/', TokenVerifyView.as_view(), name='check-token'), # Receive token
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'), # Receive refresh token
]
