from dataclasses import fields
# from users.views import User
from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

# User = get_user_model() 
 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('username', 'gender', 'phoneNumber')



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('username', 'gender', 'phoneNumber') 