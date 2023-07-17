from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password

from .models import CustomUser
from .serializers import CustomUserSerializer, RegistrationSerializer, ChangePasswordSerializer

class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')
        serializer.save(password=password)
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            return Response(
                {'access_token': str(refresh.access_token)},
                status=status.HTTP_200_OK
            )

        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Include a success message in the response
        return Response({'message': 'Password has been updated.'}, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user
