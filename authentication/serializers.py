from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'age', 'email', 'gender', 'role', 'phone']
        read_only_fields = ['id']

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'email', 'gender', 'role', 'phone', 'password']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Incorrect old password")
        return value

    def update(self, instance, validated_data):
        new_password = validated_data['new_password']
        instance.set_password(new_password)
        instance.save()
        return instance
