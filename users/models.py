from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('oth', 'Other'),
    )
    gender = models.CharField('Gender', max_length = 5, choices=GENDERS, default='' )
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True) # validators should be a list