from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.field.values():
            field.widget.attrs.update({
                "class":"form-control"
                "autocomplete":"off"
            
            })


class Loginform(AuthenticationForm):
    class Meta:
        model =User
        fields =['username','password']

    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].widget.attrs.update({
            "class":"form-control"
            "placeholder":"Username"
            "autocomplete":"off"
        })
            
        self.fields['password'].widget.attrs.update({
            "class":"form-control"
            "placeholder":"Password"
            "autocomplete":"off"
        })
            