from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegesterForm(UserCreationForm):
    # if we manually define all fields Meta.field is optional
     username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'placeholder':'Username'
        })
     )

     email = forms.EmailField(
        widget= forms.EmailInput(attrs={
            'class':'form-input',
            'placeholder':'Email address',
        })
     )

     password1= forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-input',
            'placeholder':'Password',
        })

     )
     password2= forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-input',
            'placeholder':' Confrom password',
        })

     )

     class Meta:
        model = User
        field = ['username','email','password1','password2']


class LoginForm(UserCreationForm):
     username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'placeholder':'Username',
            'autocomplete':'off',
        })
     )

     password= forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-input',
            'placeholder':'Password',
            'autocomplete':'off',
        })

     )


















        
# to use crispy form tool
# pip install django-crispy-forms,  django-crispy-bootstrap5
# Add to settings.py: Add 'crispy_forms' to INSTALLED_APPS.