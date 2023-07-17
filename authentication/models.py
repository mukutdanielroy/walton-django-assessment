from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    ]
    
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Add any additional fields if needed

    def __str__(self):
        return self.username
