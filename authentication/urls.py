from django.urls import path
from .views import RegistrationView, LoginView, ChangePasswordView, UserDetailView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]
