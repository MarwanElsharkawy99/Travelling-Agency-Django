from django import forms
from django.forms import TextInput, EmailInput,Textarea
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name',  'class': "text-field _50_percent w-input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email Address',  'class': 'text-field _50_percent w-input'}))

    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder' :'Email',  'class': 'textarea w-input'}))



class BookingForm(forms.Form):
    CHOICES=(
        ("single","single"),
        ("double","Double"),
        ("triple","Triple"),
        
    )

    NUMBERS=(
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
        ("13","13"),
        ("14","14"),
        ("15","15"),
        )
    
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full name',  }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email Address', }))
    Phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder' :'Enter the phone number',}))
    nationality= forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Enter Nationality',}))
    check_in=forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))
    check_out=forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))
    room_type=forms.ChoiceField(choices=CHOICES)
    number_of_adults=forms.ChoiceField(choices=NUMBERS)
    number_of_children=forms.ChoiceField(choices=NUMBERS)
    number_of_infants=forms.ChoiceField(choices=NUMBERS)

