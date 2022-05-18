from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
from .models import Contacto,Flan


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class FlanForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3,max_length=30)
    precio = forms.IntegerField(min_value=1,max_value=200000)
    
    class Meta:
        model = Flan
        fields = '__all__'