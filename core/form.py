from django import forms
from django.forms import TextInput, EmailInput,Textarea
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name',  'class': "text-field _50_percent w-input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email Address',  'class': 'text-field _50_percent w-input'}))

    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder' :'Email',  'class': 'textarea w-input'}))