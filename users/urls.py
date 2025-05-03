from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    RefreshTokenView,
    VerifyTokenView,
    UserProfileView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('auth/verify/', VerifyTokenView.as_view(), name='token_verify'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]