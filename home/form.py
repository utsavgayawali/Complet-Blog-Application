from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile,Post

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Username',
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Email address',
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Password',
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
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





# form for updating user and profile
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Username',
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Email address',
        })
    )
    class Meta:
        model =User
        fields =['username','email']

    
class ProfileupdateForm(forms.ModelForm):
    image = forms.ClearableFileInput(attrs={
        'class':'form-control-file'
    })
    
    bio = forms.Textarea(attrs={
        'class': 'form-textarea',
            'placeholder': 'Tell something about yourself...',
            'rows': 4
    })

    class Meta:
        model=Profile
        fields =['image','bio']



    
#  form for crating post 

class CreatePostForm(forms.ModelForm):
     title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-input',
            'placeholder': 'Post Title',
        })
    )
     content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Write your post here..',
            'rows': 4
        })
    )
     image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class':'form-control-file'
            
        })
    )

     class Meta:
        model = Post
        fields =['title','content','image']



