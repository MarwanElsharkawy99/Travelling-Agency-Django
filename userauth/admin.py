from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userauth.forms import CustomUserCreationForm,CustomUserChangeForm
from userauth.models import customUser

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm

admin.site.register(customUser ,CustomUserAdmin)
