from django import forms
from users.models import CustomUser


class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=40, help_text="enter your username")
    email = forms.EmailField(label='email', max_length=55, help_text="enter your email")
    password = forms.CharField(label='password', max_length=16, help_text="enter your password")
        
