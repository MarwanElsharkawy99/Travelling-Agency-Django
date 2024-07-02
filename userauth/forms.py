from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth.models import User

from userauth.models import customUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = customUser
        fields=['username','first_name','last_name','date_birth','nationality','mobile','Address1','Address2','city','region','zipcode','country','password1','password2','email']
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = customUser
        fields=UserChangeForm.Meta.fields



# class LoginForm(AuthenticationForm):
#     username=forms.CharField(widget=forms.TextInput({
#         'placeholder':"your Username",
#         'class':"text-field w-input"}))
#     password=forms.CharField(widget=forms.PasswordInput({
#         'placeholder':"your Password",
#         'class':"text-field w-input"}))
    
    
# class SignupForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=('username','email','password1','password2' )
#     username=forms.CharField(widget=forms.TextInput({
#         'placeholder':"your Username",
#         'class':"text-field _50_percent w-input"}))
    
#     email=forms.CharField(widget=forms.EmailInput({
#         'placeholder':"your Email",
#         'class':"text-field _50_percent w-input"}))
    
#     password1=forms.CharField(widget=forms.PasswordInput({
#         'placeholder':"your Password",
#         'class':"text-field _50_percent w-input"}))
    
#     password2=forms.CharField(widget=forms.PasswordInput({
#         'placeholder':"Repeat your password",
#         'class':"text-field _50_percent w-input"}))
    
#     # nationality=forms.CharField(widget=forms.TextInput({
#     #     'placeholder':"Enter Your nationality ",
#     #     'class':"w-full py-4 px-6 rounded-xl"}))



