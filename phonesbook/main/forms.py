from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Person

class Personform(forms.Form):
    first_name = forms.CharField(label="Imie", max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(label="Nazwisko", max_length=50)
    email = forms.EmailField(label="Email", max_length=100, required=False)
    phone_number = PhoneNumberField(region="PL", required=False)





