from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)  # General approval
    is_specially_approved = models.BooleanField(default=False)  # Special approval for 'exam' access

    TRAINING_HOSPITAL_CHOICES = [
        ('서울대병원', '서울대병원'),
        ('기타', '기타'),
    ]
    training_hospital = models.CharField(max_length=255, choices=TRAINING_HOSPITAL_CHOICES, default='기타')
