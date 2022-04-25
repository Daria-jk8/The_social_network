from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser
from users.forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    # list_display = ['username', 'gender', 'phone_Number']

    # Add user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom fields', {'fields': ('gender', 'phoneNumber',)}),
    )

    # Edit user
    fieldsets = UserAdmin.fieldsets + (
        ('Custom fields', {'fields': ('gender', 'phoneNumber',)}),
    )

    # admin.site.register(CustomUser, CustomUserAdmin)



