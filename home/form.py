from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Email address',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Password',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Confirm password',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Username',
            'autocomplete': 'off',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Password',
            'autocomplete': 'off',
        })
    )


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_pic']
#         widgets = {
#             'profile_pic': forms.FileInput(attrs={
#                 'class': 'form-control-file'
#             })
#         }
