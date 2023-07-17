from django.urls import path
from .views import RegistrationView, LoginView, ChangePasswordView, UserDetailView

urlpatterns = [
    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/user/', UserDetailView.as_view(), name='user-detail'),
]
